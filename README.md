# Tomatextor
> **Versão:** `v2.3.0`

Script Python para transcrição automática de arquivos de áudio utilizando **Faster-Whisper**. Otimizado para rodar localmente com aceleração por hardware (NVIDIA CUDA).

## Funcionalidades

* **Múltiplos Formatos:** Processamento otimizado para arquivos `.mp3` e `.m4a`.
* **Entrada e Saída Organizadas:** Áudios lidos da pasta `audios/` e transcrições salvas automaticamente na pasta `transcricoes/`, mantendo o código isolado.
* **Aceleração por GPU:** Utiliza núcleos CUDA para máxima velocidade.

## Requisitos

* **Python 3.10+**: É necessário ter o Python instalado no sistema.
* **Drivers NVIDIA & CUDA**: Para aceleração por hardware na GPU.
* **FFmpeg**: Essencial para a decodificação de áudio.
* **Fish Shell**: O script auxiliar (`.sh`) é obrigatório para usuários deste shell.

### Instalação de dependências (Arch/CachyOS)

```bash
yay -S cuda cudnn ffmpeg
```

## Instalação

1. **Clone o repositório e acesse a pasta:**
```bash
git clone https://github.com/abobrinhadigital/tomatextor-python.git
cd tomatextor
```
2. **Crie e prepare o ambiente virtual:**
```fish
python -m venv venv
source venv/bin/activate.fish
pip install torch faster-whisper
```

## Dicionário de Contexto

Para evitar que o Whisper confunda termos técnicos (ex: transformar "Jekyll" em "Jack e o"), você pode criar um arquivo chamado `dicionario.txt` na raiz do projeto.

1. Crie o arquivo: `touch dicionario.txt`
2. Adicione seus termos (um por linha ou separados por vírgula):
```text
Jekyll, venv, Python, Markdown, Pollux, Abobrinator, CLI, GitHub
```

O script lerá este arquivo automaticamente e o usará como `initial_prompt` para melhorar a precisão da transcrição.

## Configuração (.env)

O Tomatextor usa um arquivo `.env` para gerenciar os caminhos das pastas. Isso permite que ele seja integrado facilmente com outros projetos (como o Abobrinator) ou use caminhos absolutos.

1. Crie um arquivo chamado `.env` na raiz do projeto.
2. Configure as seguintes variáveis conforme sua necessidade:

```text
# Exemplo de configuração com caminhos absolutos
NEW_AUDIO_DIR="/home/usuario/audios/novos"
HISTORY_AUDIO_DIR="/home/usuario/audios/processados"
NEW_TRANSCRIPTION_DIR="/home/usuario/transcricoes/novas"
WHISPER_MODEL_SIZE="turbo"
```

*   `NEW_AUDIO_DIR`: Onde o script procura novos áudios.
*   `HISTORY_AUDIO_DIR`: Para onde os áudios processados são movidos.
*   `NEW_TRANSCRIPTION_DIR`: Onde as transcrições `.txt` são salvas.
*   `WHISPER_MODEL_SIZE`: O modelo do Whisper (ex: `tiny`, `base`, `small`, `medium`, `large-v3`, `turbo`). Padrão: `turbo`.

> [!NOTE]
> Se você não fornecer um `.env`, o script usará as pastas padrões `audios/`, `audios/processados/` e `transcricoes/`.

## Como Usar

1. Coloque seus arquivos `.mp3` ou `.m4a` dentro da pasta configurada em `NEW_AUDIO_DIR` (Padrão: `audios/`).
2. Execute o script via shell a partir da raiz do projeto:
```fish
chmod +x tomatextor.sh
./tomatextor.sh
```

---

*Este projeto é mantido sob as bênçãos do Gêmeo Imortal para a glória do Abobrinha Digital.*
