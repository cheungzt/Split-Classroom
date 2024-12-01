import pygame
import sys
from components.button import Button
from components.dialog_box import DialogBox
from constants import *
import os

class UIManager:
    def __init__(self, screen):
        self.screen = screen
        self.game = None
        self.volume = 0.5
        self.current_language = LANGUAGE_CN
        
        # 音量控制相关的属性 - 移到右上角
        self.is_dragging_volume = False
        self.volume_slider_rect = pygame.Rect(WINDOW_WIDTH - 220, 25, 200, 10)  # 右上角位置
        self.volume_handle_rect = pygame.Rect(
            self.volume_slider_rect.left + (self.volume * self.volume_slider_rect.width),
            self.volume_slider_rect.top - 5,
            10,
            20
        )
        
        # 加载英文像素字体和中文字体
        english_font = os.path.join(FONTS_DIR, "slkscrb.ttf")
        chinese_font = os.path.join(FONTS_DIR, "hanyixiangsu11pxfanti.ttf")
        
        try:
            # 字体加载...
            self.date_font = pygame.font.Font(english_font, 16)
            self.weekday_font = pygame.font.Font(english_font, 16)
            self.p_value_font = pygame.font.Font(english_font, 16)
            self.time_font = pygame.font.Font(english_font, 16)
            self.menu_font = pygame.font.Font(english_font, 28)
            self.title_font = pygame.font.Font(chinese_font, FONT_SIZE_LARGE)
            self.normal_font = pygame.font.Font(chinese_font, FONT_SIZE_MEDIUM)
            self.small_font = pygame.font.Font(chinese_font, FONT_SIZE_SMALL)
            print("成功加载字体")
        except Exception as e:
            print(f"警告：加载字体出错 - {e}")
        
        self.load_resources()
        self.init_ui_elements()
        
        # 语言切换按钮 - 左上角
        language_button_rect = pygame.Rect(25, 25, 100, 30)
        self.language_button = Button(rect=language_button_rect, color=None)
        self.language_button.text = "EN/中"
        try:
            self.language_button.font = pygame.font.Font(os.path.join(FONTS_DIR, "slkscrb.ttf"), 16)
        except:
            print("警告：无法加载slkscrb.ttf字体")
            self.language_button.font = pygame.font.Font(None, 16)
        self.language_button.text_color = WHITE
    
    def load_resources(self):
        try:
            # 加载结局画面（移到最前面加载）
            success_end_path = os.path.join(IMAGES_DIR, "happyending.png")
            fail_end_path = os.path.join(IMAGES_DIR, "badending.png")
            
            print(f"尝试加载成功结局图片: {success_end_path}")
            print(f"尝试加载失结局图片: {fail_end_path}")
            
            self.success_end_bg = pygame.image.load(success_end_path).convert()
            print("成功加载 happyending.png")
            
            self.fail_end_bg = pygame.image.load(fail_end_path).convert()
            print("成功加载 badending.png")
            
            # 加载其他背景
            self.menu_bg = pygame.image.load(os.path.join(IMAGES_DIR, "gamestart.png")).convert()
            print("成功加载 gamestart.png")
            
            self.intro_bg = pygame.image.load(os.path.join(IMAGES_DIR, "intro_bg.png")).convert()
            print("成功加载 intro_bg.png")
            
            self.story_bg = pygame.image.load(os.path.join(IMAGES_DIR, "story_bg.png")).convert()
            print("成功加载 story_bg.png")
            
            # 加载学生头像并确保尺寸一致
            base_avatar = pygame.image.load(os.path.join(IMAGES_DIR, "normal.png")).convert_alpha()
            base_size = base_avatar.get_size()  # 使用normal.png的尺寸作为标准
            self.student_avatars = {
                "normal": base_avatar,
                "up": pygame.transform.scale(
                    pygame.image.load(os.path.join(IMAGES_DIR, "P_up.png")).convert_alpha(),
                    base_size
                ),
                "down": pygame.transform.scale(
                    pygame.image.load(os.path.join(IMAGES_DIR, "P_down.png")).convert_alpha(),
                    base_size
                ),
                "over80": pygame.transform.scale(
                    pygame.image.load(os.path.join(IMAGES_DIR, "P_over80.png")).convert_alpha(),
                    base_size
                )
            }
            print(f"成功加载所有学生头像，标准尺寸: {base_size}")
            
            # 加载老师头像
            self.teacher_avatars = {
                "Simon": pygame.image.load(os.path.join(IMAGES_DIR, "teacher_simon.png")).convert_alpha(),
                "Anthony": pygame.image.load(os.path.join(IMAGES_DIR, "teacher_anthony.png")).convert_alpha(),
                "David": pygame.image.load(os.path.join(IMAGES_DIR, "teacher_david.png")).convert_alpha(),
                "Gio": pygame.image.load(os.path.join(IMAGES_DIR, "teacher_gio.png")).convert_alpha(),
                "Henry": pygame.image.load(os.path.join(IMAGES_DIR, "teacher_henry.png")).convert_alpha()
            }
            
            # 加载UI元素
            self.date_box = pygame.image.load(os.path.join(IMAGES_DIR, "date_box.png")).convert_alpha()
            print("成功加载 date_box.png")
            
            self.weekday_box = pygame.image.load(os.path.join(IMAGES_DIR, "weekday_box.png")).convert_alpha()
            print("成功加载 weekday_box.png")
            
            self.p_value_box = pygame.image.load(os.path.join(IMAGES_DIR, "p_value_box.png")).convert_alpha()
            print("成功加载 p_value_box.png")
            
            self.time_box = pygame.image.load(os.path.join(IMAGES_DIR, "time_box.png")).convert_alpha()
            print("成功加载 time_box.png")
            
            self.choice_panel = pygame.image.load(os.path.join(IMAGES_DIR, "choice_panel.png")).convert_alpha()
            print("成功加载 choice_panel.png")
            
            self.choice_button = pygame.image.load(os.path.join(IMAGES_DIR, "choice_button.png")).convert_alpha()
            print("成功加载 choice_button.png")
            
            self.dialog_student = pygame.image.load(os.path.join(IMAGES_DIR, "dialog_student.png")).convert_alpha()
            print("成功加载 dialog_student.png")
            
            self.dialog_teacher = pygame.image.load(os.path.join(IMAGES_DIR, "dialog_teacher.png")).convert_alpha()
            print("成功加载 dialog_teacher.png")
            
            # 加载确认按钮图片
            self.confirm_img = pygame.image.load(os.path.join(IMAGES_DIR, "cofirm.png")).convert_alpha()
            print("成功加载 cofirm.png")
            
        except Exception as e:
            print(f"警告：无法加载图片资源 - {e}")
            print(f"IMAGES_DIR路径: {IMAGES_DIR}")
            import traceback
            traceback.print_exc()
        
        # 加载音效
        try:
            pygame.mixer.init()
            self.bgm = pygame.mixer.Sound(os.path.join(SOUNDS_DIR, "bgm.mp3"))
            self.bgm.set_volume(self.volume)  # 设置初始音量
            self.click_sound = pygame.mixer.Sound(os.path.join(SOUNDS_DIR, "click.wav"))
            self.choice_click_sound = pygame.mixer.Sound(os.path.join(SOUNDS_DIR, "choice_click.wav"))
            self.click_sound.set_volume(self.volume)
            self.choice_click_sound.set_volume(self.volume)
            print("成功加载音频资源")
        except Exception as e:
            print(f"警告：无法加载音频资源 - {e}")
    
    def init_ui_elements(self):
        """初始化UI元素"""
        # 开
        start_button_rect = pygame.Rect(553, 389, 174, 56)
        self.start_button = Button(rect=start_button_rect, color=None)
        self.start_button.text = "START"
        try:
            self.start_button.font = pygame.font.Font(os.path.join(FONTS_DIR, "slkscrb.ttf"), 20)
        except:
            self.start_button.font = pygame.font.Font(None, 20)
        self.start_button.text_color = WHITE
        
        # 退出游戏按钮
        quit_button_rect = pygame.Rect(553, 479, 174, 56)
        self.quit_button = Button(rect=quit_button_rect, color=None)
        self.quit_button.text = "QUIT"
        try:
            self.quit_button.font = pygame.font.Font(os.path.join(FONTS_DIR, "slkscrb.ttf"), 20)
        except:
            self.quit_button.font = pygame.font.Font(None, 20)
        self.quit_button.text_color = WHITE
        
        # 继续按钮
        continue_button_rect = pygame.Rect(1170, 634, 37, 20)
        self.continue_button = Button(rect=continue_button_rect, color=None)
        self.continue_button.text = "继续" if self.current_language == LANGUAGE_CN else "Continue"

        # 选项按钮
        self.choice_buttons = []
        for i in range(3):
            choice_rect = pygame.Rect(100, 300 + i * 100, 600, 50)
            choice_button = Button(rect=choice_rect, color=None)
            choice_button.text = f"选项 {chr(65+i)}" if self.current_language == LANGUAGE_CN else f"Option {chr(65+i)}"
            self.choice_buttons.append(choice_button)

    def start_game_action(self):
        if self.game:
            self.game.state = STATE_INTRO
            
    def quit_game_action(self):
        pygame.quit()
        sys.exit()
        
    def toggle_language(self):
        """切换语言"""
        self.current_language = LANGUAGE_EN if self.current_language == LANGUAGE_CN else LANGUAGE_CN
        print(f"切换语言到: {self.current_language}")
        
        # 同步语言设置到游戏对象
        if self.game:
            self.game.current_language = self.current_language
            # 如果在反馈状态，更新反馈文本
            if self.game.state == STATE_FEEDBACK:
                if hasattr(self.game, 'last_choice'):
                    choice = self.game.last_choice
                    self.game.current_feedback = self.game.story_manager.get_feedback_text(choice, self.current_language)
                    print(f"更新反馈文本，选项: {choice}, 语言: {self.current_language}")
        
        # 更新所有按钮的文本
        self.init_ui_elements()
    
    def continue_action(self):
        if self.game:
            self.game.handle_story_click((1170, 634))
            
    def choice_action(self, index):
        if self.game:
            self.game.handle_choice_click((self.choice_buttons[index].rect.centerx, 
                                         self.choice_buttons[index].rect.centery))

    def draw_menu(self):
        """绘制菜单界面"""
        # 使用gamestart.png作为背景
        if hasattr(self, 'menu_bg'):
            scaled_bg = pygame.transform.scale(self.menu_bg, (WINDOW_WIDTH, WINDOW_HEIGHT))
            self.screen.blit(scaled_bg, (0, 0))
        else:
            self.screen.fill((50, 50, 50))
        
        # 绘制按钮，传递 screen 参数
        self.start_button.draw(self.screen)
        self.quit_button.draw(self.screen)
        self.language_button.draw(self.screen)
        
        # 绘制音量控制
        self.draw_volume_control()
    
    def handle_volume_event(self, event):
        """处理音量控制相关的事件"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 左键点击
                if self.volume_slider_rect.collidepoint(event.pos):
                    self.is_dragging_volume = True
                    # 立即更新音量
                    new_x = max(self.volume_slider_rect.left, 
                              min(event.pos[0], self.volume_slider_rect.right))
                    self.volume = (new_x - self.volume_slider_rect.left) / self.volume_slider_rect.width
                    self.volume_handle_rect.centerx = new_x
                    self.update_volume()
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # 左键放
                self.is_dragging_volume = False
        
        elif event.type == pygame.MOUSEMOTION and self.is_dragging_volume:
            # 计算新的音量值（0-1之间）
            new_x = max(self.volume_slider_rect.left, 
                       min(event.pos[0], self.volume_slider_rect.right))
            self.volume = (new_x - self.volume_slider_rect.left) / self.volume_slider_rect.width
            self.volume_handle_rect.centerx = new_x
            self.update_volume()
    
    def update_volume(self):
        """更新所有音频的音量"""
        if hasattr(self, 'bgm'):
            self.bgm.set_volume(self.volume)
        if hasattr(self, 'click_sound'):
            self.click_sound.set_volume(self.volume)
        if hasattr(self, 'choice_click_sound'):
            self.choice_click_sound.set_volume(self.volume)
    
    def draw_volume_control(self):
        """绘制音量控制滑块"""
        # 绘制滑块背景
        pygame.draw.rect(self.screen, (100, 100, 100), self.volume_slider_rect)
        
        # 绘制已填充部分
        filled_rect = pygame.Rect(
            self.volume_slider_rect.left,
            self.volume_slider_rect.top,
            int(self.volume_slider_rect.width * self.volume),
            self.volume_slider_rect.height
        )
        pygame.draw.rect(self.screen, (200, 200, 200), filled_rect)
        
        # 绘制滑块手柄
        pygame.draw.rect(self.screen, (255, 255, 255), self.volume_handle_rect)
        
        # 绘制音量文本
        try:
            volume_font = pygame.font.Font(os.path.join(FONTS_DIR, "slkscrb.ttf"), 16)
        except:
            volume_font = pygame.font.Font(None, 16)
        
        volume_text = f"VOLUME: {int(self.volume * 100)}%"
        text_surface = volume_font.render(volume_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(
            right=self.volume_slider_rect.left - 10,
            centery=self.volume_slider_rect.centery
        )
        self.screen.blit(text_surface, text_rect)
    
    def play_click_sound(self):
        """放普通按钮效"""
        if hasattr(self, 'click_sound'):
            self.click_sound.play()

    def play_choice_click_sound(self):
        """播放选项钮音效"""
        if hasattr(self, 'choice_click_sound'):
            self.choice_click_sound.play()
    
    def play_bgm(self):
        """播放背景音乐"""
        if hasattr(self, 'bgm'):
            try:
                self.bgm.play(-1)  # -1表循环播放
                self.bgm.set_volume(self.volume)  # 设置初始音量
                print("开始放BGM")
            except Exception as e:
                print(f"播放BGM时出错: {e}")
    
    def stop_bgm(self):
        if hasattr(self, 'bgm'):
            self.bgm.stop()
        
    def draw_base_ui(self):
        """绘制基础UI元素，所有状态都会用到"""
        # 绘制背景
        if hasattr(self, 'story_bg'):
            scaled_bg = pygame.transform.scale(self.story_bg, (WINDOW_WIDTH, WINDOW_HEIGHT))
            self.screen.blit(scaled_bg, (0, 0))
        else:
            self.screen.fill(PURPLE_BG)
            
        # 绘制对话框
        if hasattr(self, 'dialog_student'):
            self.screen.blit(self.dialog_student, (310, 50))  # 学生对话框
            
        if hasattr(self, 'dialog_teacher'):
            self.screen.blit(self.dialog_teacher, (830, 50))  # 老师对话框
            
        # 获前老师的字并显示对应头像
        current_teacher = self.get_current_teacher_name()
        if hasattr(self, 'teacher_avatars') and current_teacher in self.teacher_avatars:
            self.screen.blit(self.teacher_avatars[current_teacher], (866, 111))  # 老师头像
            print(f"显示{current_teacher}老师的头像")  # 调试信息
        else:
            print(f"警告：找不到{current_teacher}老师的头像")  # 调试信息
            
        # 绘制选项面板
        if hasattr(self, 'choice_panel'):
            self.screen.blit(self.choice_panel, (50, WINDOW_HEIGHT - 350 - 50))
            
        # 绘制学生头像
        if hasattr(self, 'student_avatars') and self.game:
            avatar_state = self.game.student_avatar_state if hasattr(self.game, 'student_avatar_state') else "normal"
            avatar = self.student_avatars.get(avatar_state, self.student_avatars["normal"])
            # 获取头像尺寸以计算居中位置
            avatar_width, avatar_height = avatar.get_size()
            x = 360  # 固定x坐标
            y = 111  # 固定y坐标
            print(f"绘制头像 - 状态: {avatar_state}, 位置: ({x}, {y}), 尺寸: {avatar_width}x{avatar_height}")
            self.screen.blit(avatar, (x, y))
            
    def get_bilingual_text(self, cn_text, en_text):
        """根据当���语言返回对应文本"""
        return cn_text if self.current_language == LANGUAGE_CN else en_text
    
    def draw_story(self, story_text):
        """绘制故事文本"""
        try:
            # 先绘制基础UI
            self.draw_base_ui()
            
            # 绘制语言切换按钮
            if hasattr(self, 'language_button'):
                self.language_button.draw(self.screen)
            
            # 绘制左侧信息栏UI元素
            if hasattr(self, 'date_box'):
                self.screen.blit(self.date_box, (50, 50))
                month, day = self.game.start_date
                current_day = day + self.game.current_day - 1
                date_text = f"SEP {current_day}"
                date_surface = self.date_font.render(date_text, True, WHITE)
                date_x = 50 + (115 - date_surface.get_width()) - 10
                date_y = 50 + (70 - date_surface.get_height()) // 2
                self.screen.blit(date_surface, (date_x, date_y))
            
            if hasattr(self, 'weekday_box'):
                self.screen.blit(self.weekday_box, (175, 50))
                weekdays_en = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
                weekday = weekdays_en[self.game.current_day - 1]
                weekday_surface = self.weekday_font.render(weekday, True, WHITE)
                weekday_x = 175 + (115 - weekday_surface.get_width()) - 10
                weekday_y = 50 + (70 - weekday_surface.get_height()) // 2
                self.screen.blit(weekday_surface, (weekday_x, weekday_y))
            
            if hasattr(self, 'p_value_box'):
                self.screen.blit(self.p_value_box, (50, 130))
                p_text = f"P-VALUE: {self.game.p_value}%"
                p_surface = self.p_value_font.render(p_text, True, WHITE)
                p_text_x = 120
                p_text_y = 150
                self.screen.blit(p_surface, (p_text_x, p_text_y))
                
                # 进度条
                bar_width = 150
                bar_height = 20
                bar_x = 120
                bar_y = p_text_y + p_surface.get_height() + 5
                pygame.draw.rect(self.screen, LIGHT_GRAY, (bar_x, bar_y, bar_width, bar_height))
                progress_width = int((self.game.p_value / 100) * bar_width)
                color = BRIGHT_RED if self.game.p_value >= 80 else DARK_RED
                pygame.draw.rect(self.screen, color, (bar_x, bar_y, progress_width, bar_height))
            
            if hasattr(self, 'time_box'):
                self.screen.blit(self.time_box, (50, 240))
                if self.game.current_time is not None:
                    time_text = self.game.format_time(self.game.current_time)
                    time_surface = self.time_font.render(time_text, True, WHITE)
                    time_x = 50 + (240 - time_surface.get_width()) - 10
                    time_y = 240 + (70 - time_surface.get_height()) // 2
                    self.screen.blit(time_surface, (time_x, time_y))
            
            # 获取要显示的文本
            if isinstance(story_text, dict):
                display_text = story_text.get(self.current_language, "")
            else:
                display_text = story_text
                
            try:
                font = pygame.font.Font(os.path.join(FONTS_DIR, "hanyixiangsu11pxfanti.ttf"), FONT_SIZE_MEDIUM)
            except:
                font = pygame.font.Font(None, FONT_SIZE_MEDIUM)
            
            # 设置文本框参数
            text_box_x = 857  # 距左边857像素
            text_box_y = 359  # 距顶部359像素
            text_box_width = 350  # 文本框宽度
            text_box_height = 269  # 文本框高度
            padding = 30  # 文本边距
            line_spacing = 1  # 减小行距到1像素
            
            # 处理文本
            lines = []
            paragraphs = str(display_text).split('\n')
            
            for paragraph in paragraphs:
                if not paragraph.strip():
                    lines.append("")
                    continue
                
                current_line = ""
                words = list(paragraph)
                
                for word in words:
                    test_line = current_line + word
                    if font.size(test_line)[0] <= text_box_width - (padding * 2):
                        current_line = test_line
                    else:
                        if current_line:
                            lines.append(current_line)
                        current_line = word
                
                if current_line:
                    lines.append(current_line)
                lines.append("")  # 段落之间添加空行
            
            if lines and not lines[-1].strip():
                lines.pop()
            
            # 计算总文本高度
            total_height = len(lines) * (font.get_height() + line_spacing)
            
            # 计算起始y坐标以实现垂直居中
            start_y = text_box_y + (text_box_height - total_height) // 2
            
            # 绘制文本
            for line in lines:
                text_surface = font.render(line, True, BLACK)
                text_rect = text_surface.get_rect()
                # 水平居中
                text_rect.centerx = text_box_x + text_box_width // 2
                text_rect.top = start_y
                self.screen.blit(text_surface, text_rect)
                start_y += font.get_height() + line_spacing
            
            # 绘制继续按钮
            if hasattr(self, 'confirm_img'):
                self.screen.blit(self.confirm_img, (1170, 634))
            
            # 绘制音量控制
            self.draw_volume_control()
            
        except Exception as e:
            print(f"绘制故事时出错: {e}")
            import traceback
            traceback.print_exc()
    
    def draw_choices(self, choices):
        """绘制选项"""
        try:
            # 先绘制基础UI
            self.draw_base_ui()
            
            # 绘制语言切换按钮
            if hasattr(self, 'language_button'):
                self.language_button.draw(self.screen)
            
            # 绘制左侧信息栏UI元素
            if hasattr(self, 'date_box'):
                self.screen.blit(self.date_box, (50, 50))
                month, day = self.game.start_date
                current_day = day + self.game.current_day - 1
                date_text = f"SEP {current_day}"
                date_surface = self.date_font.render(date_text, True, WHITE)
                date_x = 50 + (115 - date_surface.get_width()) - 10
                date_y = 50 + (70 - date_surface.get_height()) // 2
                self.screen.blit(date_surface, (date_x, date_y))
            
            if hasattr(self, 'weekday_box'):
                self.screen.blit(self.weekday_box, (175, 50))
                weekdays_en = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
                weekday = weekdays_en[self.game.current_day - 1]
                weekday_surface = self.weekday_font.render(weekday, True, WHITE)
                weekday_x = 175 + (115 - weekday_surface.get_width()) - 10
                weekday_y = 50 + (70 - weekday_surface.get_height()) // 2
                self.screen.blit(weekday_surface, (weekday_x, weekday_y))
            
            if hasattr(self, 'p_value_box'):
                self.screen.blit(self.p_value_box, (50, 130))
                p_text = f"P-VALUE: {self.game.p_value}%"
                p_surface = self.p_value_font.render(p_text, True, WHITE)
                p_text_x = 120
                p_text_y = 150
                self.screen.blit(p_surface, (p_text_x, p_text_y))
                
                # 进度条
                bar_width = 150
                bar_height = 20
                bar_x = 120
                bar_y = p_text_y + p_surface.get_height() + 5
                pygame.draw.rect(self.screen, LIGHT_GRAY, (bar_x, bar_y, bar_width, bar_height))
                progress_width = int((self.game.p_value / 100) * bar_width)
                color = BRIGHT_RED if self.game.p_value >= 80 else DARK_RED
                pygame.draw.rect(self.screen, color, (bar_x, bar_y, progress_width, bar_height))
            
            if hasattr(self, 'time_box'):
                self.screen.blit(self.time_box, (50, 240))
                if self.game.current_time is not None:
                    time_text = self.game.format_time(self.game.current_time)
                    time_surface = self.time_font.render(time_text, True, WHITE)
                    time_x = 50 + (240 - time_surface.get_width()) - 10
                    time_y = 240 + (70 - time_surface.get_height()) // 2
                    self.screen.blit(time_surface, (time_x, time_y))
            
            # 绘制选项按钮图片
            if hasattr(self, 'choice_button'):
                # 更新按钮的点击区域并绘制按钮图片
                self.choice_buttons[0].rect = pygame.Rect(144, 356, 49, 49)  # A选项
                self.choice_buttons[1].rect = pygame.Rect(144, 476, 49, 49)  # B选项
                self.choice_buttons[2].rect = pygame.Rect(144, 588, 49, 49)  # C选项
                self.screen.blit(self.choice_button, (144, 356))
            
            # 如果有预览的选项，显示在学生对话框中
            if hasattr(self.game, 'preview_choice') and self.game.preview_choice:
                try:
                    font = pygame.font.Font(os.path.join(FONTS_DIR, "hanyixiangsu11pxfanti.ttf"), FONT_SIZE_MEDIUM)
                except:
                    font = pygame.font.Font(None, FONT_SIZE_MEDIUM)
                
                # 获取当前语言的预览文本
                if isinstance(self.game.preview_choice, dict):
                    preview_text = self.game.preview_choice.get(self.current_language, 
                                                              self.game.preview_choice.get(LANGUAGE_CN))
                else:
                    preview_text = self.game.preview_choice
                
                # 移除选项前缀（A. B. C.）
                if isinstance(preview_text, str) and preview_text.startswith(('A.', 'B.', 'C.')):
                    preview_text = preview_text[2:].strip()
                
                # 设置文本框参数
                text_box_x = 395  # 距左边395像素
                text_box_y = 395  # 距顶部395像素
                text_box_width = 350  # 文本框宽度
                text_box_height = 200  # 文本框高度
                padding = 30  # 文本边距
                line_spacing = 1  # 减小行距到1像素
                
                # 处理文本换行
                lines = []
                paragraphs = str(preview_text).split('\n')
                
                for paragraph in paragraphs:
                    if not paragraph.strip():
                        lines.append("")
                        continue
                    
                    current_line = ""
                    words = list(paragraph)
                    
                    for word in words:
                        test_line = current_line + word
                        if font.size(test_line)[0] <= text_box_width - (padding * 2):
                            current_line = test_line
                        else:
                            if current_line:
                                lines.append(current_line)
                            current_line = word
                    
                    if current_line:
                        lines.append(current_line)
                
                # 计算总文本高度
                total_height = len(lines) * (font.get_height() + line_spacing)
                
                # 计算起始y坐标以实现垂直居中
                start_y = text_box_y + (text_box_height - total_height) // 2
                
                # 绘制文本
                for line in lines:
                    text_surface = font.render(line, True, BLACK)
                    text_rect = text_surface.get_rect()
                    # 水平居中
                    text_rect.centerx = text_box_x + text_box_width // 2
                    text_rect.top = start_y
                    self.screen.blit(text_surface, text_rect)
                    start_y += font.get_height() + line_spacing
            
            # 只有选择了选项才显示确认按钮
            if self.game.selected_choice is not None:
                if hasattr(self, 'confirm_img'):
                    self.screen.blit(self.confirm_img, (1170, 634))
            
            self.draw_volume_control()
            
        except Exception as e:
            print(f"绘制选项时出错: {e}")
            import traceback
            traceback.print_exc()
    
    def draw_feedback(self, feedback_text):
        # 先绘制基础UI
        self.draw_base_ui()
        
        # 绘制语言切换按钮
        if hasattr(self, 'language_button'):
            self.language_button.draw(self.screen)
            
        # 绘制左侧信息栏UI元素
        if hasattr(self, 'date_box'):
            self.screen.blit(self.date_box, (50, 50))
            month, day = self.game.start_date
            current_day = day + self.game.current_day - 1
            date_text = f"SEP {current_day}"
            date_surface = self.date_font.render(date_text, True, WHITE)
            date_x = 50 + (115 - date_surface.get_width()) - 10
            date_y = 50 + (70 - date_surface.get_height()) // 2
            self.screen.blit(date_surface, (date_x, date_y))
        
        if hasattr(self, 'weekday_box'):
            self.screen.blit(self.weekday_box, (175, 50))
            weekdays_en = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
            weekday = weekdays_en[self.game.current_day - 1]
            weekday_surface = self.weekday_font.render(weekday, True, WHITE)
            weekday_x = 175 + (115 - weekday_surface.get_width()) - 10
            weekday_y = 50 + (70 - weekday_surface.get_height()) // 2
            self.screen.blit(weekday_surface, (weekday_x, weekday_y))
        
        if hasattr(self, 'p_value_box'):
            self.screen.blit(self.p_value_box, (50, 130))
            
            # P值文本
            p_text = f"P-VALUE: {self.game.p_value}%"
            p_surface = self.p_value_font.render(p_text, True, WHITE)
            p_text_x = 120
            p_text_y = 150
            self.screen.blit(p_surface, (p_text_x, p_text_y))
            
            # 进度条
            bar_width = 150
            bar_height = 20
            bar_x = 120
            bar_y = p_text_y + p_surface.get_height() + 5
            
            pygame.draw.rect(self.screen, LIGHT_GRAY, (bar_x, bar_y, bar_width, bar_height))
            progress_width = int((self.game.p_value / 100) * bar_width)
            color = BRIGHT_RED if self.game.p_value >= 80 else DARK_RED
            pygame.draw.rect(self.screen, color, (bar_x, bar_y, progress_width, bar_height))
        
        if hasattr(self, 'time_box'):
            self.screen.blit(self.time_box, (50, 240))
            if self.game.current_time is not None:
                time_text = self.game.format_time(self.game.current_time)
                time_surface = self.time_font.render(time_text, True, WHITE)
                time_x = 50 + (240 - time_surface.get_width()) - 10
                time_y = 240 + (70 - time_surface.get_height()) // 2
                self.screen.blit(time_surface, (time_x, time_y))
        
        # 在学生对话框中显示选择的文本
        if hasattr(self.game, 'current_choice'):
            if isinstance(self.game.current_choice, dict):
                choice_text = self.game.current_choice.get(self.current_language, 
                                                         self.game.current_choice.get(LANGUAGE_CN))
            else:
                choice_text = self.game.current_choice
            
            if isinstance(choice_text, str) and choice_text.startswith(('A.', 'B.', 'C.')):
                choice_text = choice_text[2:].strip()
            
            try:
                font = pygame.font.Font(os.path.join(FONTS_DIR, "hanyixiangsu11pxfanti.ttf"), FONT_SIZE_MEDIUM)
            except:
                font = pygame.font.Font(None, FONT_SIZE_MEDIUM)
            
            # 处理学生对话框文本
            max_width = 350  # 学生对话框宽度
            lines = []
            paragraphs = choice_text.split('\n')
            
            for paragraph in paragraphs:
                if not paragraph.strip():
                    lines.append("")
                    continue
                
                current_line = ""
                words = list(paragraph)
                
                for word in words:
                    test_line = current_line + word
                    if font.size(test_line)[0] <= max_width:
                        current_line = test_line
                    else:
                        if current_line:
                            lines.append(current_line)
                        current_line = word
                
                if current_line:
                    lines.append(current_line)
                lines.append("")
            
            if lines and not lines[-1].strip():
                lines.pop()
            
            # 计算总文本高度以居中显示
            line_spacing = 8
            total_height = len(lines) * (font.get_height() + line_spacing)
            start_y = 359 + (269 - total_height) // 2
            
            # 在学生对话框中绘制文本
            for line in lines:
                text_surface = font.render(line, True, BLACK)
                text_rect = text_surface.get_rect()
                text_rect.centerx = 360 + 400 // 2
                text_rect.top = start_y
                self.screen.blit(text_surface, text_rect)
                start_y += font.get_height() + line_spacing
        
        # 在老师对话框中显示反馈文本
        if feedback_text:
            try:
                font = pygame.font.Font(os.path.join(FONTS_DIR, "hanyixiangsu11pxfanti.ttf"), FONT_SIZE_MEDIUM)
            except:
                font = pygame.font.Font(None, FONT_SIZE_MEDIUM)
            
            # 设置老师对话框的文本参数
            text_box_x = 857  # 距左边857像素
            text_box_y = 359  # 距顶部359像素
            text_box_width = 350  # 文本���宽度
            text_box_height = 269  # 文本框高度
            padding = 30  # 文本边距
            line_spacing = 1  # 减小行距到1像素
            
            # 获取要显示的文本
            if isinstance(feedback_text, dict):
                display_text = feedback_text.get(self.current_language, "")
            else:
                display_text = feedback_text
            
            # 如果反馈文本为空，尝试获取另一种语言的文本
            if not display_text and isinstance(feedback_text, dict):
                other_language = LANGUAGE_EN if self.current_language == LANGUAGE_CN else LANGUAGE_CN
                display_text = feedback_text.get(other_language, "")
            
            # 处理老师对话框文本
            lines = []
            paragraphs = str(display_text).split('\n')
            
            for paragraph in paragraphs:
                if not paragraph.strip():
                    lines.append("")
                    continue
                
                current_line = ""
                words = list(paragraph)
                
                for word in words:
                    test_line = current_line + word
                    if font.size(test_line)[0] <= text_box_width - (padding * 2):  # 考虑边距
                        current_line = test_line
                    else:
                        if current_line:
                            lines.append(current_line)
                        current_line = word
                
                if current_line:
                    lines.append(current_line)
                lines.append("")  # 段落之间添加空行
            
            if lines and not lines[-1].strip():
                lines.pop()
            
            # 计算总文本高度
            total_height = len(lines) * (font.get_height() + line_spacing)
            
            # 计算起始y坐标以实现垂直居中
            start_y = text_box_y + (text_box_height - total_height) // 2
            
            # 绘制文本
            for line in lines:
                text_surface = font.render(line, True, BLACK)
                text_rect = text_surface.get_rect()
                # 水平居中
                text_rect.centerx = text_box_x + text_box_width // 2
                text_rect.top = start_y
                self.screen.blit(text_surface, text_rect)
                start_y += font.get_height() + line_spacing
        
        # 绘制继续按钮
        if hasattr(self, 'confirm_img'):
            try:
                self.screen.blit(self.confirm_img, (1170, 634))
            except Exception as e:
                print(f"绘制确认按钮图片时出错: {e}")
        
        self.draw_volume_control()
    
    def draw_game_over(self):
        try:
            # 修改判断逻辑：如果P值到100，显示失败结局，否则显示成功结局
            if self.game.p_value >= 100:  # P值达到100，显示失败结局
                if hasattr(self, 'fail_end_bg'):
                    scaled_bg = pygame.transform.scale(self.fail_end_bg, (WINDOW_WIDTH, WINDOW_HEIGHT))
                    self.screen.blit(scaled_bg, (0, 0))
                    print("显示失结局画面 (badending.png)")
                else:
                    print("警告：找不到badending.png")
                    self.screen.fill((50, 50, 50))
            else:  # P值未达到100，显示成功结局
                if hasattr(self, 'success_end_bg'):
                    scaled_bg = pygame.transform.scale(self.success_end_bg, (WINDOW_WIDTH, WINDOW_HEIGHT))
                    self.screen.blit(scaled_bg, (0, 0))
                    print("显示成功结局画面 (happyending.png)")
                else:
                    print("警告：找不到happyending.png")
                    self.screen.fill((50, 50, 50))
            
            # 绘制音量控制
            self.draw_volume_control()
            
        except Exception as e:
            print(f"绘制结束画面时出错: {e}")
            import traceback
            traceback.print_exc()
    
    def draw_p_value(self, p_value):
        # 绘制P值进度条
        bar_width = 200
        bar_height = 20
        x = WINDOW_WIDTH - bar_width - 20
        y = 20
        
        # 条
        pygame.draw.rect(self.screen, LIGHT_GRAY, 
                        (x, y, bar_width, bar_height))
        
        # P值进度
        progress_width = int((p_value / 100) * bar_width)
        color = GREEN if p_value < 70 else RED
        pygame.draw.rect(self.screen, color,
                        (x, y, progress_width, bar_height))
        
        # P值文本 - 使用中文字体
        try:
            font = pygame.font.Font(os.path.join(FONTS_DIR, "hanyixiangsu11pxfanti.ttf"), FONT_SIZE)
        except:
            font = pygame.font.Font(None, FONT_SIZE)
        text = font.render(f"P值: {p_value}%", True, BLACK)
        self.screen.blit(text, (x - 80, y)) 

    def set_game(self, game):
        self.game = game 

    def draw_intro(self, story_text):
        # 使用intro_bg.png作为背景
        if hasattr(self, 'intro_bg'):
            scaled_bg = pygame.transform.scale(self.intro_bg, (WINDOW_WIDTH, WINDOW_HEIGHT))
            self.screen.blit(scaled_bg, (0, 0))
        else:
            self.screen.fill(PURPLE_BG)
        
        # 文本框的精确位置和大小
        text_box_width = 519  # 精确的文本框宽度
        text_box_height = 581  # 精确的文本框高度
        text_box_x = 380  # 距左边380像素
        text_box_y = 69   # 距离顶69像素
        padding = 20      # 边距
        
        # 设置字体大小（调小一点以适应文本框）
        try:
            font = pygame.font.Font(os.path.join(FONTS_DIR, "hanyixiangsu11pxfanti.ttf"), 18)  # 减小字体大小
        except:
            font = pygame.font.Font(None, 18)
            
        # 绘制语言切换按钮
        if hasattr(self, 'language_button'):
            self.language_button.draw(self.screen)
        
        # 获取双语文本
        if isinstance(story_text, dict):
            display_text = story_text.get(self.current_language)
            print(f"当前语言: {self.current_language}, 显示文本: {display_text}")  # 调试信息
        else:
            display_text = story_text
            print(f"使用原始文本: {display_text}")  # 调试信息
        
        # 绘制文本
        if display_text:
            # 分行处理文本
            max_width = text_box_width - padding * 2
            lines = []
            
            # 先按换行符分割文本
            paragraphs = display_text.split('\n')  # 使用单个反斜杠
            print(f"分割后的段落: {paragraphs}")  # 调试信息
            
            for paragraph in paragraphs:
                if not paragraph.strip():  # 如果是空段落，直接添加空行
                    lines.append("")
                    continue
                    
                current_line = ""
                words = list(paragraph)  # 将段落分成字符列表
                
                for word in words:
                    test_line = current_line + word
                    # 检查添加新字符是否超出宽度
                    if font.size(test_line)[0] <= max_width:
                        current_line = test_line
                    else:
                        if current_line:
                            lines.append(current_line)
                        current_line = word
                
                if current_line:  # 添加最后一行
                    lines.append(current_line)
                lines.append("")  # 段落之间添加空行
            
            if lines and not lines[-1].strip():  # 如果最后一行是空行，删除它
                lines.pop()
            
            print(f"处理后的行: {lines}")  # 调试信息
            
            # 计算总文本高度
            line_spacing = 8
            total_height = len(lines) * (font.get_height() + line_spacing)
            
            # 调整起始y坐标，使文本垂直居中
            y = text_box_y + (text_box_height - total_height) // 2
            
            # 绘制文本
            for line in lines:
                text_surface = font.render(line, True, WHITE)
                text_rect = text_surface.get_rect()
                # 水平居中对齐
                text_rect.centerx = text_box_x + text_box_width // 2
                text_rect.top = y
                self.screen.blit(text_surface, text_rect)
                y += font.get_height() + line_spacing
        
        # 继续按钮（使用英文像素字体）
        try:
            continue_font = pygame.font.Font(os.path.join(FONTS_DIR, "slkscrb.ttf"), 20)
        except Exception as e:
            print(f"加载继续按钮字体出错: {e}")
            continue_font = pygame.font.Font(None, 20)
        
        # 创建继续按钮
        continue_button_rect = pygame.Rect(
            563,  # 距离左边563像素
            540,  # 距离顶部540像素
            171,  # 宽度171像素
            58    # 高度58像素
        )
        self.continue_button = Button(rect=continue_button_rect, color=None)  # 透明背景
        self.continue_button.text = "CONTINUE"  # 英文文本
        self.continue_button.text_color = WHITE  # 白色文字
        self.continue_button.font = continue_font  # 使用新字体
        
        # 检查文本是否超出按钮宽度
        text_surface = continue_font.render("CONTINUE", True, WHITE)
        if text_surface.get_width() > continue_button_rect.width - 20:  # 留出10像素边距
            # 如果文本太长，缩小字体大小
            continue_font = pygame.font.Font(os.path.join(FONTS_DIR, "slkscrb.ttf"), 16)
            self.continue_button.font = continue_font
        
        self.continue_button.draw(self.screen)
    
    def get_current_teacher_name(self):
        """根据当前天数获取对应的老师名字"""
        teacher_schedule = {
            1: "Simon",    # 周一 - Simon老师
            2: "Anthony",  # 周二 - Anthony老师
            3: "David",    # 周三 - David老师
            4: "Gio",      # 周四 - Gio老师
            5: "Henry",    # 周五 - Henry老师
            6: "Simon",    # 周六 - Simon老师
            7: "David"     # 周日 - David老师（修改为David）
        }
        return teacher_schedule.get(self.game.current_day, "Simon")
    
    def is_clicked(self, pos):
        """检查给定位置是否点击了按钮"""
        button_rect = pygame.Rect(1170, 634, 37, 20)
        return button_rect.collidepoint(pos)
    
    def handle_language_button(self, pos):
        """处理语言切换按钮点击
        Args:
            pos: 鼠标点击位置
        Returns:
            bool: 是否点击了语言切换按钮
        """
        if hasattr(self, 'language_button') and self.language_button.is_clicked(pos):
            self.play_click_sound()
            self.toggle_language()
            return True
        return False
