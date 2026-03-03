# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.3.0] - 2026-03-03

### Added
- Modelo Whisper agora é configurável via variável `WHISPER_MODEL_SIZE` no `.env`.
- Upgrade do modelo padrão para `turbo` (mais rápido e inteligente para contextos mistos).
- Otimização do `initial_prompt` com contexto fixo de tecnologia para melhorar a precisão de termos técnicos (ex: "vibe code").

## [2.2.0] - 2026-03-03

### Added
- Suporte a variáveis de ambiente via arquivo `.env`.
- Carregamento manual de configurações para evitar dependências extras.
- Suporte a caminhos absolutos e tratamento de aspas nas configurações de diretórios.
- Novas variáveis de configuração: `NEW_AUDIO_DIR`, `HISTORY_AUDIO_DIR` e `NEW_TRANSCRIPTION_DIR`.

### Fixed
- Pequeno "desastre" visual no footer do `README.md`.

## [2.1.0] - 2026-03-02

### Added
- Suporte para transcrição de arquivos `.m4a` (solicitação do mestre para o post de hoje).
- Implementação de versionamento semântico (`__version__` no código).
- Este arquivo de `CHANGELOG.md` para que o Pollux não tenha que ler a mente do mestre no futuro.
- Atualização do `README.md` detalhando os formatos suportados.

## [Antiguidade] - Infinito até 2026-03-01

### Added
- **O Grande Caos Original**: Versões que existiram apenas na cabeça distraída do mestre ou em scripts sem nome.
- **Marcação Pré-histórica**: Segundo as escritas sagradas do mestre, nada disso conta porque ele "ainda não tinha inventado que queria marcação". Foram tempos sombrios onde os dinossauros (e os bugs) vagavam sem versão.

> [!NOTE]
> Esta seção existe apenas para satisfazer o ego retrospectivo do meu mestre e a curiosidade arqueológica do Pollux.
