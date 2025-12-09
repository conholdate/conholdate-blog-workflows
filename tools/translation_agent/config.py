DOMAIN_ASPOSE_COM           = "blog.aspose.com"
DOMAIN_GROUPDOCS_COM        = "blog.groupdocs.com"
DOMAIN_CONHOLDATE_COM       = "blog.conholdate.com"
DOMAIN_ASPOSE_CLOUD         = "blog.aspose.cloud"
DOMAIN_GROUPDOCS_CLOUD      = "blog.groupdocs.cloud"
DOMAIN_CONHOLDATE_CLOUD     = "blog.conholdate.cloud"


# KEYS ==========================================
KEY_SHEET_ID            = "sheet_id"
KEY_LOCAL_GITHUB_REPO   = "local_github_repo"
KEY_SUPPORTED_LANGS     = "langs"
KEY_MENTIONS_AUTHOR     = "mentions"
KEY_IS_SEND_EMAIL       = "Send Email"
SEND_EMAIL_TRUE         = "Y"
SEND_EMAIL_FALSE        = "-"

# SHEET IDS =====================================
SHEET_ID_ASPOSE_COM         = "1gxx6xk2HJ7IPpRsvLG7Ef18jc7BnQuAAJ33UyHn8b3w"
SHEET_ID_GROUPDOCS_COM      = "1H8M5ZTBdSFRTuYMjzn-O0gRDX6beIB50t55g6dOPWoA"
SHEET_ID_CONHOLDATE_COM     = "10vzH3ZBiURAXamt0VOppYODKZNmDt0LR_zYXb13YJhs"
SHEET_ID_ASPOSE_CLOUD       = "1HcHQxooeva8iwnDmee-SX07KNKke5sXjWC6ZPJw1G0o"
SHEET_ID_GROUPDOCS_CLOUD    = "1x0Jx0yniKjGMcccmb_2JPJylVP6EIWeN-H2UOC6Y47U"
SHEET_ID_CONHOLDATE_CLOUD   = "1Ofoc8f-jbguE4rUGkKNLFvLObxPll9s3_Hw97UsZizs"

SHEET_ID_TEST_QA        = "1LC7-DgkxufOqdmipJ-s-p_FZLixH0n6pNnPkIJjjqbc"
SHEET_ID_SUMMARY        = "1G_Q_shGbNXJCp-xu_maqFZWddpB-VksQh_Ni0OfxDts"

# LOCAL GITHUB REPOS ============================
LOC_GIT_REPO_ASPOSE_COM         = "blog-checkedout-repo/content/Aspose.Blog"
LOC_GIT_REPO_GROUPDOCS_COM      = "blog-checkedout-repo/content/Groupdocs.Blog"
LOC_GIT_REPO_CONHOLDATE_COM     = "blog-checkedout-repo/content/Conholdate.Total"
LOC_GIT_REPO_ASPOSE_CLOUD       = "blog-checkedout-repo/content/Aspose.Cloud"
LOC_GIT_REPO_GROUPDOCS_CLOUD    = "blog-checkedout-repo/content/GroupDocs.Cloud"
LOC_GIT_REPO_CONHOLDATE_CLOUD   = "blog-checkedout-repo/content/Conholdate.Cloud"

# SUPPORTED LANGUAGES ===========================
LANGS_ASPOSE_COM        = "ar|cs|de|es|fa|fr|he|id|it|ja|ko|pl|pt|ru|sv|th|tr|uk|vi|zh|zh-hant"
LANGS_GROUPDOCS_COM     = "ar|cs|de|es|fa|fr|he|id|it|ja|ko|nl|pl|pt|ru|th|tr|uk|vi|zh|zh-hant"
LANGS_CONHOLDATE_COM    = "ar|de|es|fa|fr|id|it|ja|ko|nl|pl|pt|ru|th|tr|vi|zh|cs"
LANGS_ASPOSE_CLOUD      = "ar|da|de|el|es|fa|fr|he|hu|it|ja|ka|ko|pt|ru|th|tr|uk|vi|zh|zh-tw"
LANGS_GROUPDOCS_CLOUD   = "ar|de|es|fa|fr|id|it|ja|ko|pl|pt|ru|th|tr|uk|vi|zh|zh-hant"
LANGS_CONHOLDATE_CLOUD  = "ar|cs|de|es|fa|fr|he|id|it|ja|ko|nl|pl|pt|ru|sv|th|tr|uk|vi|zh|zh-hant"

DEV_ALEXANDER_HRAMOV     = "@alexanderhramov"
DEV_DENIS_GVARDIONOV     = "@denisgvardionov"
DEV_FARHAN               = "@farhanrazablog"
DEV_JOHN_HE              = "@johnhenanjing"
DEV_MARGARITA            = "@margaritasamodurova"
DEV_MARY_GERASIMOVA      = "@marygerasimova"
DEV_MUSTAFA              = "@mustafabutt69"
DEV_MUZAMMIL_KHAN        = "@muzammilzkhan"
DEV_NAYYER               = "@codewarior"
DEV_PETR_SHALAMOV        = "@petrshalamov"
DEV_ROY_WANG             = "@asposeroywang"
DEV_SERGEY_TERESHCHENKO  = "@sergiytereshchenko"
DEV_SHOAIB_KHAN          = "@mshoaibkhankk"
DEV_YANA_LITVINCHIK      = "@yanalitvinchik"
DEV_VLADIMIR_LITVINCHIK  = "@vlitvinchik"
DEV_GROUPDOCS_TEAM       = "@vlitvinchik"
DEV_YURIY_MAZURCHUK      = "@ymazurchuk"


DEV = {
    "Alexander Hramov"      : DEV_ALEXANDER_HRAMOV,
    "Denis Gvardionov"      : DEV_DENIS_GVARDIONOV,
    "Farhan Raza"           : DEV_FARHAN,
    "John He"               : DEV_JOHN_HE,
    "Margarita Samodurova"  : DEV_MARGARITA,
    "Mary Gerasimova"       : DEV_MARY_GERASIMOVA,
    "Muhammad Mustafa"      : DEV_MUSTAFA,
    "Muzammil Khan"         : DEV_MUZAMMIL_KHAN,
    "Nayyer Shahbaz"        : DEV_NAYYER,
    "Petr Shalamov"         : DEV_PETR_SHALAMOV,
    "Roy Wang"              : DEV_ROY_WANG,
    "Sergey Tereshchenko"   : DEV_SERGEY_TERESHCHENKO,
    "Shoaib Khan"           : DEV_SHOAIB_KHAN,
    "Yana Litvinchik"       : DEV_YANA_LITVINCHIK,
    "Vladimir Litvinchik"   : DEV_VLADIMIR_LITVINCHIK,
    "GroupDocs Team"        : DEV_GROUPDOCS_TEAM,
    "Yuriy Mazurchuk"       : DEV_YURIY_MAZURCHUK    
}

# Normalize keys
DEV_NORMALIZED = {k.lower(): v for k, v in DEV.items()}

# Spreadsheet IDs / Keys
domains_data = {
    DOMAIN_ASPOSE_COM         : {
        KEY_SHEET_ID          :   SHEET_ID_ASPOSE_COM,
        KEY_LOCAL_GITHUB_REPO :   LOC_GIT_REPO_ASPOSE_COM,
        KEY_SUPPORTED_LANGS   :   LANGS_ASPOSE_COM,
        KEY_MENTIONS_AUTHOR          :   [DEV_MUZAMMIL_KHAN, DEV_MUSTAFA, DEV_SHOAIB_KHAN],
        KEY_IS_SEND_EMAIL     :   SEND_EMAIL_FALSE
    },
    DOMAIN_GROUPDOCS_COM      : {
        KEY_SHEET_ID          :   SHEET_ID_GROUPDOCS_COM,
        KEY_LOCAL_GITHUB_REPO :   LOC_GIT_REPO_GROUPDOCS_COM,
        KEY_SUPPORTED_LANGS   :   LANGS_GROUPDOCS_COM,
        KEY_MENTIONS_AUTHOR          :   [DEV_SHOAIB_KHAN],
        KEY_IS_SEND_EMAIL     :   SEND_EMAIL_FALSE
    },
    DOMAIN_CONHOLDATE_COM     : {
        KEY_SHEET_ID          :   SHEET_ID_CONHOLDATE_COM,
        KEY_LOCAL_GITHUB_REPO :   LOC_GIT_REPO_CONHOLDATE_COM,
        KEY_SUPPORTED_LANGS   :   LANGS_CONHOLDATE_COM,
        KEY_MENTIONS_AUTHOR          :   [DEV_FARHAN, DEV_SHOAIB_KHAN],
        KEY_IS_SEND_EMAIL     :   SEND_EMAIL_FALSE
    },
    DOMAIN_ASPOSE_CLOUD       : {
        KEY_SHEET_ID          :   SHEET_ID_ASPOSE_CLOUD,
        KEY_LOCAL_GITHUB_REPO :   LOC_GIT_REPO_ASPOSE_CLOUD,
        KEY_SUPPORTED_LANGS   :   LANGS_ASPOSE_CLOUD,
        KEY_MENTIONS_AUTHOR          :   [DEV_NAYYER, DEV_SHOAIB_KHAN],
        KEY_IS_SEND_EMAIL     :   SEND_EMAIL_FALSE
    },
    DOMAIN_GROUPDOCS_CLOUD    : {
        KEY_SHEET_ID          :   SHEET_ID_GROUPDOCS_CLOUD,
        KEY_LOCAL_GITHUB_REPO :   LOC_GIT_REPO_GROUPDOCS_CLOUD,
        KEY_SUPPORTED_LANGS   :   LANGS_GROUPDOCS_CLOUD,
        KEY_MENTIONS_AUTHOR          :   [DEV_NAYYER, DEV_SHOAIB_KHAN],
        KEY_IS_SEND_EMAIL     :   SEND_EMAIL_FALSE
    },
    DOMAIN_CONHOLDATE_CLOUD    : {
        KEY_SHEET_ID          :   SHEET_ID_CONHOLDATE_CLOUD,
        KEY_LOCAL_GITHUB_REPO :   LOC_GIT_REPO_CONHOLDATE_CLOUD,
        KEY_SUPPORTED_LANGS   :   LANGS_CONHOLDATE_CLOUD,
        KEY_MENTIONS_AUTHOR          :   [DEV_FARHAN, DEV_SHOAIB_KHAN],
        KEY_IS_SEND_EMAIL     :   SEND_EMAIL_FALSE
    }
}

# HEADERS for Missing Translations ==============
KEY_PRODUCT_NAME    = "Product"
KEY_DIR_BASE        = "Blog Post Directory"
KEY_AUTHOR          = "Author"
KEY_MISSING_COUNT   = "Missing Count"
KEY_MISSING_FILES   = "Missing Translations"
KEY_EXTRA_FILES     = "Extra Translations"
KEY_EXTRA_COUNT     = "Extra Files Count"
KEY_STATUS          = "Status"

# ===== HEADERS for SUMMARY SHEET ===============
KEY_DATE                = "Date"
KEY_DOMAIN              = "Domain"
KEY_INVALID_FOLDER_COUNT= "Invalid Folder Count"
KEY_AUTHORS             = "Authors"
KEY_SPREADSHEET_LINK    = "Details Spreadsheet"

HEADERS_MISSING_TRANSLATIONS = [ 
    KEY_DOMAIN,
    KEY_PRODUCT_NAME,
    KEY_DIR_BASE,
    KEY_AUTHOR,
    KEY_MISSING_COUNT,
    KEY_MISSING_FILES,
    KEY_EXTRA_FILES,
    KEY_EXTRA_COUNT,
    KEY_STATUS
]


# "Date", "Domain", "Invalid Folder Count", "Authors", "Details Spreadsheet"
HEADERS_SUMMARY = [
    KEY_DATE,
    KEY_DOMAIN,
    KEY_INVALID_FOLDER_COUNT,
    KEY_AUTHORS,
    KEY_SPREADSHEET_LINK,
    KEY_IS_SEND_EMAIL
]

PRODUCT_MAP = {
    # Aspose Product Family
    "aspose.3d"         : "3d",
    "aspose.barcode"    : "barcode",
    "aspose.cad"        : "cad",
    "aspose.cells"      : "cells",
    "aspose.diagram"    : "diagram",
    "aspose.drawing"    : "drawing",
    "aspose.email"      : "email",
    "aspose.finance"    : "finance",
    "aspose.font"       : "font",
    "aspose.gis"        : "gis",
    "aspose.html"       : "html",
    "aspose.imaging"    : "imaging",
    "aspose.note"       : "note",
    "aspose.ocr"        : "ocr",
    "aspose.omr"        : "omr",
    "aspose.page"       : "page",
    "aspose.pdf"        : "pdf",
    "aspose.psd"        : "psd",
    "aspose.pub"        : "pub",
    "aspose.slides"     : "slides",
    "aspose.svg"        : "svg",
    "aspose.tasks"      : "tasks",
    "aspose.tex"        : "tex",
    "aspose.total"      : "total",
    "aspose.words"      : "words",
    "aspose.zip"        : "zip",
    "aspose.medical"    : "medical",

    # Aspose Cloud Product Family
    "aspose.3d cloud"       : "3d",
    "aspose.barcode cloud"  : "barcode",
    "aspose.cad cloud"      : "cad",
    "aspose.cells cloud"    : "cells",
    "aspose.diagram cloud"  : "diagram",
    "aspose.email cloud"    : "email",
    "aspose.html cloud"     : "html",
    "aspose.imaging cloud"  : "imaging",
    "aspose.ocr cloud"      : "ocr",
    "aspose.omr cloud"      : "omr",
    "aspose.pdf cloud"      : "pdf",
    "aspose.slides cloud"   : "slides",
    "aspose.tasks cloud"    : "tasks",
    "aspose.total cloud"    : "total",
    "aspose.words cloud"    : "words",

    # GroupDocs Product Family
    "groupdocs.annotation"      : "annotation",
    "groupdocs.assembly"        : "assembly",
    "groupdocs.classification"  : "classification",
    "groupdocs.comparison"      : "comparison",
    "groupdocs.conversion"      : "conversion",
    "groupdocs.editor"          : "editor",
    "groupdocs.markdown"        : "markdown",
    "groupdocs.merger"          : "merger",
    "groupdocs.metadata"        : "metadata",
    "groupdocs.parser"          : "parser",
    "groupdocs.redaction"       : "redaction",
    "groupdocs.search"          : "search",
    "groupdocs.signature"       : "signature",
    "groupdocs.total"           : "total",
    "groupdocs.viewer"          : "viewer",
    "groupdocs.watermark"       : "watermark",

    # GroupDocs Cloud Product Family
    "groupdocs.annotation cloud"    : "annotation",
    "groupdocs.assembly cloud"      : "assembly",
    "groupdocs.classification cloud": "classification",
    "groupdocs.comparison cloud"    : "comparison",
    "groupdocs.conversion cloud"    : "conversion",
    "groupdocs.editor cloud"        : "editor",
    "groupdocs.merger cloud"        : "merger",
    "groupdocs.metadata cloud"      : "metadata",
    "groupdocs.parser cloud"        : "parser",
    "groupdocs.rewriter cloud"      : "rewriter",
    "groupdocs.signature cloud"     : "signature",
    "groupdocs.total cloud"         : "total",
    "groupdocs.translation cloud"   : "translation",
    "groupdocs.viewer cloud"        : "viewer",
    "groupdocs.watermark cloud"     : "watermark",

    # Conholdate Product Family
    "conholdate.total"          : "total",

    # Conholdate Cloud Product Family
    "conholdate.total cloud"    : "total",

    # Aspose - SHORT NAMES
    "3d"            : "3d",
    "barcode"       : "barcode",
    "cad"           : "cad",
    "cells"         : "cells",
    "diagram"       : "diagram",
    "drawing"       : "drawing",
    "email"         : "email",
    "finance"       : "finance",
    "font"          : "font",
    "gis"           : "gis",
    "html"          : "html",
    "imaging"       : "imaging",
    "medical"       : "medical",
    "note"          : "note",
    "ocr"           : "ocr",
    "omr"           : "omr",
    "page"          : "page",
    "pdf"           : "pdf",
    "psd"           : "psd",
    "pub"           : "pub",
    "slides"        : "slides",
    "svg"           : "svg",
    "tasks"         : "tasks",
    "tex"           : "tex",
    "words"         : "words",
    "zip"           : "zip",

    # GroupDocs - SHORT NAMES
    "annotation"    : "annotation",
    "assembly"      : "assembly",
    "classification": "classification",
    "comparison"    : "comparison",
    "conversion"    : "conversion",
    "editor"        : "editor",
    "markdown"      : "markdown",
    "merger"        : "merger",
    "metadata"      : "metadata",
    "parser"        : "parser",
    "redaction"     : "redaction",
    "rewriter"      : "rewriter",
    "search"        : "search",
    "signature"     : "signature",
    "translation"   : "translation",
    "viewer"        : "viewer",
    "watermark"     : "watermark",

    # Combined - SHORT NAMES
    "total"         : "total",


}