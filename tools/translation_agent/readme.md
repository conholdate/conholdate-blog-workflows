# Blogs Translation Agent

Automated translation system for blog posts across multiple domains and languages with daily scanning and quality validation.

---

## 🎯 Overview

A two-part automation system that:
1. **Scans** blog repositories daily for missing translations
2. **Translates** blog posts into 20+ languages with AI-powered quality checks

---

## ✨ Features

- ✅ **Automated Daily Scanning** - Detects missing translations across all domains
- ✅ **Smart Translation** - AI-powered with retry logic and quality validation
- ✅ **Format Preservation** - Maintains markdown formatting, code blocks, and links
- ✅ **Front-matter Protection** - Never translates product names or critical metadata
- ✅ **Multi-domain Support** - Works across 6 blog domains
- ✅ **22 Languages** - Comprehensive language coverage
- ✅ **GitHub Actions Integration** - Automated daily workflows

---

## 📋 Prerequisites

- Python 3.13+
- API key for translation service (Professionalize LLM)
- Google Sheets API credentials (for scanning reports)
- GitHub/GitLab access tokens (for repository operations)

---

## 🚀 Installation

### 1. Clone Repository

```bash
git clone https://gitlab.recruitize.ai/sialkot/lahore-aspose/lahore-blogs-team/blog-post-translator
cd blog-post-translator
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r tools/translation_agent/requirements.txt
```

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file or set these environment variables:

```bash
# Required for scanning
GOOGLE_CREDENTIALS_JSON_SK=<your-google-credentials-json>

# Required for translation
PROFESSIONALIZE_LLM_API_KEY=<your-api-key>

```

### Config Files

- `config.py` - Domain configurations, language mappings, author handles
- `requirements.txt` - Python dependencies

---

## 📖 Usage

### Part 1: Scan for Missing Translations

Scans blog repositories and generates reports in Google Sheets.

```bash
python tools/translation_agent/scan_missing_translations.py --domain <DOMAIN>
```

**Options:**
- `--domain` (required) - Target domain or "all"

**Example:**
```bash
python tools/translation_agent/scan_missing_translations.py \
  --domain blog.aspose.com \
  --key sk-xxxxxxxxx
```

---

### Part 2: Translate Blog Posts

Translates blog posts into missing languages.

```bash
python tools/translation_agent/translator.py \
  --domain <DOMAIN> \
  --key <API_KEY> \
  [--product <PRODUCT>] \
  [--author <AUTHOR>] \
  [--limit <NUMBER>]
```

**Required Parameters:**
- `--domain` - Target blog domain
- `--key` - API key (sk-xxxxxxxxx)

**Optional Parameters:**
- `--product` - Specific product (e.g., email, cells, conversion)
- `--author` - Author name (e.g., "Muhammad Mustafa")
- `--limit` - Number of posts to translate

---

## 🌍 Supported Domains

- `blog.aspose.com`
- `blog.groupdocs.com`
- `blog.conholdate.com`
- `blog.aspose.cloud`
- `blog.groupdocs.cloud`
- `blog.conholdate.cloud`

---

## 🗣️ Languages

This supports translation into all languages and its output is tested on the following languages:

```
ar (Arabic)         | cs (Czech)       | de (German)      | es (Spanish)
fa (Persian)        | fr (French)      | he (Hebrew)      | id (Indonesian)
it (Italian)        | ja (Japanese)    | ko (Korean)      | nl (Dutch)
pl (Polish)         | pt (Portuguese)  | ru (Russian)     | sv (Swedish)
th (Thai)           | tr (Turkish)     | uk (Ukrainian)   | vi (Vietnamese)
zh (Chinese)        | zh-hant (Chinese Traditional)
```

**Total: 22 languages**

---

## 🏗️ Architecture

### Components

```
blog-post-translator/
├── tools/translation_agent/
│   ├── scan_missing_translations.py   # Scanner component
│   ├── translator.py                  # Translation component
│   ├── config.py                      # Configuration
│   ├── io_google_spreadsheet.py       # Google Sheets integration
│   └── requirements.txt               # Dependencies
├── .github/workflows/
│   ├── scan-missing-translations.yml  # Daily scan workflow
│   └── translate-blogs.yml            # Manual translation workflow
└── README.md
```

### Translation Agents

**TranslationOrchestrator**
- Coordinates the translation workflow
- Manages agent interactions
- Handles file I/O operations

**FrontmatterTranslatorAgent**
- Translates YAML frontmatter fields
- Protects product names and metadata
- Updates URLs with language prefixes

**ContentTranslatorAgent**
- Translates markdown content
- Preserves formatting and code blocks
- Implements retry logic with AI validation

---

## 🤖 GitHub Actions

### Daily Scan Workflow

Runs automatically at 01:00 UTC daily.

**File:** `.github/workflows/scan-missing-translations.yml`

**Trigger:** Scheduled (cron) or manual dispatch

**Matrix:** Runs for all 6 domains in parallel

### Manual Translation Workflow

Trigger manually via GitHub Actions UI.

**File:** `.github/workflows/translate-blogs.yml`

**Inputs:**
- Domain (dropdown)
- Product (dropdown, optional)
- Author (text, optional)
- Limit (number, optional)

---

## 📊 Reports

Scan results are automatically saved to Google Sheets with:
- Domain
- Product name
- Blog post directory
- Author
- Missing translation count
- Missing languages list
- Extra/invalid files
- Direct links to details

**Summary Sheet:** Aggregated daily reports across all domains

---

## 🔒 Security

- **API Keys:** Store in GitHub Secrets or environment variables
- **Google Credentials:** Use service account with minimal permissions
- **GitHub Tokens:** Use Personal Access Tokens (PAT) with repo scope only
- **Never commit:** `.env` files, API keys, or credentials

---

## 🐛 Troubleshooting

### Translation Fails

**Issue:** `401 Authentication Error`
- **Solution:** Verify API key is valid and active

**Issue:** Translation returns untranslated content
- **Solution:** Tool automatically retries up to 3 times with enhanced prompts

### Scan Fails

**Issue:** `Spreadsheet not found`
- **Solution:** Check Google credentials and sheet permissions

**Issue:** Repository not accessible
- **Solution:** Verify GitHub/GitLab token has correct permissions

### Common Errors

**Code blocks not preserved**
- Tool automatically detects and skips translation validation for code blocks
- If issues persist, check markdown formatting

---