import os

# Window settings
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
TITLE = "Split Classroom"

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE_BG = (230, 230, 250)
DUSTY_PINK = (255, 228, 225)
SAGE_GREEN = (230, 238, 230)
GOLDEN = (255, 223, 186)
LIGHT_GRAY = (211, 211, 211)
TRANSPARENT_RED = (255, 200, 200, 128)  # 浅红色，Alpha=128表示半透明
PINK = (255, 192, 203)       # 粉色
BRIGHT_RED = (255, 0, 0)     # 亮红色
DARK_RED = (139, 0, 0)      # 暗红色

# Font sizes
FONT_SIZE_LARGE = 28    # 标题字体大小
FONT_SIZE_MEDIUM = 14   # 正常文本大小（对话框文字，调小）
FONT_SIZE_SMALL = 18    # 选项ABC字体大小（改大）
FONT_SIZE = 10         # 默认字体大小

# UI settings
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
DIALOG_PADDING = 10

# Game states
STATE_MENU = "menu"
STATE_INTRO = "intro"
STATE_STORY = "story"
STATE_CHOICE = "choice"
STATE_FEEDBACK = "feedback"
STATE_RESULT = "result"

# 字体设置 - 使用新的像素字体
CHINESE_FONT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                           "assets", "fonts", "ark-pixel-12px-monospaced-zh_cn.otf")

# 资源路径
ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
SOUNDS_DIR = os.path.join(ASSETS_DIR, "sounds")
FONTS_DIR = os.path.join(ASSETS_DIR, "fonts")

# Language settings
LANGUAGE_CN = "cn"
LANGUAGE_EN = "en"