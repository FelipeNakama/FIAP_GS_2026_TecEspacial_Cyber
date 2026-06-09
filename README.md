# Sistema de Monitoramento de Lixo Espacial — Módulo DevSecOps

## Sobre o Projeto
Plataforma de rastreamento de detritos orbitais com IA preditiva e alertas em tempo real.
Este repositório contém a implementação do módulo DevSecOps da Global Solution FIAP 2026.

**Integrantes:**
- Felipe Megumi Nakama — RM 552821
- Luís Alberto Rocha Filho — RM 553507
- Micael Santos Azarias — RM 552699
- Nathan da Silveira Uflacker — RM 553264

## Pipeline de Segurança (GitHub Actions)

O pipeline executa automaticamente a cada push na branch main:

| Stage | Ferramenta | Controle |
|-------|-----------|----------|
| 1 - Secret Scan | Detector customizado (grep) | Gestão de Segredos |
| 2 - Dependency Scan | pip-audit | Ferramentas CI/CD (SCA) |
| 3 - Container Scan | Trivy | Segurança em Contêineres |
| 4 - Notificação | GitHub Actions (if: failure()) | Auditoria Contínua |

## Decisões Técnicas

### Stage 1 — Detector customizado de secrets
O detector utiliza `grep` para identificar atribuições diretas de credenciais conhecidas
do projeto (ex.: `NASA_API_KEY`) no código-fonte. Essa abordagem foi adotada por ser
mais precisa para secrets específicos do projeto, eliminando falsos negativos de
ferramentas genéricas que dependem de verificação online do token.

### Stage 3 — .trivyignore
O Trivy identificou CVEs nos pacotes internos de build da imagem base (`wheel` e
`jaraco.context`). Como esses pacotes são usados apenas durante o build e não são
expostos em tempo de execução, foram documentados no `.trivyignore`, seguindo a
prática recomendada para gerenciar falsos positivos em pipelines de produção.

## Como os Secrets são Gerenciados

Credenciais (ex.: `NASA_API_KEY`) são armazenadas em:
**Settings → Secrets and variables → Actions**

Nunca são escritas diretamente no código-fonte. O Stage 1 do pipeline bloqueia
qualquer commit que viole essa regra.

## Estrutura do Repositório
```
FIAP_GS_2026_TecEspacial_Cyber/
├── .github/
│   └── workflows/
│       └── devsecops.yml    # Pipeline principal
├── app/
│   └── main.py              # Aplicação Flask
├── evidencias/              # Prints e logs das execuções
├── .trivyignore             # CVEs documentados de ferramentas de build
├── Dockerfile
├── requirements.txt
└── README.md
```

## Evidências

As evidências da execução do pipeline estão na pasta `/evidencias/`:

| Arquivo | Descrição |
|---------|-----------|
| Print 1 | Secret NASA_API_KEY configurado no GitHub Secrets |
| Print 2 | Pipeline completo com todos os stages verdes |
| Print 3 | Log do pip-audit com 13 CVEs detectados (Stage 2) |
| Print 4 | Log do Trivy com imagem aprovada após .trivyignore (Stage 3) |
| Print 5 | NASA_API_KEY hardcoded no main.py (simulação) |
| Print 6 | Stage 1 detectando a key exposta e bloqueando o pipeline |
| Print 7 | Stage 4 notificando o autor da falha |
| Print 8 | Pipeline passando após correção |

## Conexão com o Projeto GS

Este módulo integra segurança ao Sistema de Monitoramento de Lixo Espacial,
garantindo que dados orbitais críticos e credenciais de agências espaciais
(NASA, ESA) sejam protegidos ao longo de todo o ciclo de vida do software.

## ODS Relacionados

| ODS | Conexão |
|-----|---------|
| ODS 9 | Inovação em infraestrutura tecnológica espacial segura |
| ODS 11 | Satélites protegidos suportam GPS, comunicações e logística urbana |
| ODS 13 | Integridade de satélites de monitoramento ambiental |
| ODS 16 | Governança responsável de tecnologia espacial de uso dual |
