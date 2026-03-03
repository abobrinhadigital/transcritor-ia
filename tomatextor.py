import datetime
import glob
import os
import shutil
import torch
from faster_whisper import WhisperModel

__version__ = "2.1.0"

# Carregando bibliotecas da Nvidia (Otimizado para RTX 3050)
model_size = "medium"
model = WhisperModel(model_size, device="cuda", compute_type="float16")

# Define as pastas do projeto
pasta_audios = "audios"
pasta_processados = os.path.join(pasta_audios, "processados")
pasta_transcricoes = "transcricoes"

# Cria as pastas caso elas ainda não existam
os.makedirs(pasta_processados, exist_ok=True)
os.makedirs(pasta_transcricoes, exist_ok=True)

# Busca todos os arquivos .mp3 e .m4a na pasta audios/ (ignora os que já estão em processados/)
formatos = ["*.mp3", "*.m4a"]
arquivos = []
for formato in formatos:
    arquivos.extend(glob.glob(os.path.join(pasta_audios, formato)))

if not arquivos:
    print(f"Nenhum arquivo de áudio novo (.mp3 ou .m4a) encontrado na pasta {pasta_audios}/")
    exit()

print(f"Encontrado(s) {len(arquivos)} arquivo(s) para processar.\n")

# Carrega o dicionário/prompt inicial se o arquivo existir
caminho_dicionario = "dicionario.txt"
if os.path.exists(caminho_dicionario):
    with open(caminho_dicionario, "r", encoding="utf-8") as f:
        # Lê as linhas, remove espaços em branco e junta tudo com vírgulas
        termos = [linha.strip() for linha in f.readlines() if linha.strip()]
        prompt_inicial = ", ".join(termos)
else:
    prompt_inicial = None

# Processa cada arquivo encontrado na pasta
for input_audio in arquivos:
    nome_base_audio = os.path.basename(input_audio)
    print(f"--- Processando: {nome_base_audio} na GPU ---")

    # --- Lógica de Nomeação para Jekyll ---
    data_hoje = datetime.datetime.now().strftime('%Y-%m-%d')
    prefixo = f"{data_hoje}-transcricao"

    # Conta arquivos existentes de hoje para definir o número (ex: -1.txt, -2.txt)
    # Isso fica dentro do loop para garantir que cada áudio ganhe um número novo!
    numero_sequencial = len(glob.glob(os.path.join(pasta_transcricoes, f"{prefixo}-*.txt"))) + 1
    nome_arquivo_txt = f"{prefixo}-{numero_sequencial}.txt"
    output_text = os.path.join(pasta_transcricoes, nome_arquivo_txt)

    # Transcrição
    #segments, info = model.transcribe(input_audio, beam_size=5, language="pt")
    segments, info = model.transcribe(
        input_audio, 
        beam_size=5, 
        language="pt",
        initial_prompt=prompt_inicial
    )

    # Abre o arquivo para salvar o texto
    with open(output_text, "w", encoding="utf-8") as f:
        for segment in segments:
            texto_limpo = segment.text.strip()
            print(texto_limpo) # Mostra no terminal para você acompanhar
            f.write(texto_limpo + "\n") # Salva no arquivo

    print(f"\n✅ Texto salvo em: {output_text}")

    # Move o arquivo de áudio processado para a subpasta
    caminho_destino = os.path.join(pasta_processados, nome_base_audio)
    shutil.move(input_audio, caminho_destino)
    print(f"📁 Áudio original movido para: {caminho_destino}\n")

print("🎉 Processamento em lote concluído com sucesso!")