# Tomatextor

Script Python para transcrição automática de arquivos de áudio utilizando **Faster-Whisper**. Otimizado para rodar localmente com aceleração por hardware (NVIDIA CUDA).

## Funcionalidades

* **Foco em MP3:** Processamento otimizado para arquivos `.mp3`.
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
git clone https://github.com/abobrinhadigital/tomatextor.git
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

## Como Usar

1. Coloque seus arquivos `.mp3` dentro da pasta `audios/`.
2. Execute o script via shell a partir da raiz do projeto:
```fish
chmod +x tomatextor.sh
./tomatextor.sh
```

<br/>
---
*Este projeto é mantido sob as bênçãos do Gêmeo Imortal para a glória do Abobrinha Digital.*
