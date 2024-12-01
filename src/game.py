import pygame
import sys
from story_manager import StoryManager
from ui_manager import UIManager
from constants import *
from components.button import Button

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.story_manager = StoryManager()
        self.ui_manager = UIManager(screen)
        self.ui_manager.set_game(self)
        self.state = STATE_MENU
        self.p_value = 50
        self.last_p_value = 50  # 添加上一次P值记录
        self.current_day = 1
        self.current_feedback = None
        self.selected_choice = None
        self.preview_choice = None
        self.current_language = LANGUAGE_CN
        self.student_avatar_state = "normal"  # 设置初始头像状态
        
        # 添加日期和时间管理
        self.start_date = (9, 2)  # 9月2号开始
        self.weekdays = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
        self.time_ranges = {
            "早上": ["9:30", "10:30", "11:30"],
            "下午": ["13:30", "14:30", "15:30", "16:30", "17:30"],
            "晚上": ["19:00", "19:45", "20:30", "21:15"]
        }
        
        # 添加每个老师的具体时间段
        self.teacher_times = {
            "Simon": {"morning": "10:30-12:30", "afternoon": "13:30-17:30"},
            "Anthony": {"morning": "9:30-11:30", "afternoon": "12:30-18:30"},
            "David": {"afternoon": "13:30-17:30"},
            "Gio": {"morning": "9:30-11:30", "afternoon": "12:30-18:30"},
            "Henry": "any"  # 任意时间
        }
        
        # 时间管理
        self.game_time = None  # 游戏开始时间
        self.current_time = None  # 当前游戏时间
        self.time_start_tick = None  # 开始计时的时刻
        self.last_p_value_update = None  # 上次更新P值的时间
        self.time_pressure_interval = 5  # 每5秒检查一次（游戏中的5分钟）
        self.time_pressure_penalty = 5  # P值增加量
        self.time_running = False  # 控制时间是否流逝
        self.p_value_active = False  # 控制是否增加P值
        
        # 根据当前故事随机生成一个时间点
        self.generate_game_time()
        
        # 开始播放BGM
        self.ui_manager.play_bgm()
        
        # 创建按钮
        self.create_buttons()
        
    def generate_game_time(self):
        """根据当前故事生成一个时间点"""
        import random
        time_range = self.story_manager.get_current_time_range()
        if time_range:
            # 随机选择一个时间点
            start_time = time_range[0]
            self.game_time = self.convert_time_to_minutes(start_time)
            self.current_time = self.game_time
            
    def convert_time_to_minutes(self, time_str):
        """将时间字符串转换为分钟数"""
        hours, minutes = map(int, time_str.split(':'))
        return hours * 60 + minutes
        
    def format_time(self, minutes):
        """将分钟数转换为时间字符串"""
        hours = minutes // 60
        mins = minutes % 60
        return f"{hours:02d}:{mins:02d}"
        
    def handle_event(self, event):
        # 处理音量控制事件
        self.ui_manager.handle_volume_event(event)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 先检查语言切换按钮
            if self.ui_manager.handle_language_button(event.pos):
                # 更新当前显示的文本
                if self.state == STATE_FEEDBACK:
                    # 获取当前选择的选项
                    choice = None
                    for i, button in enumerate(self.ui_manager.choice_buttons):
                        if button.is_clicked(event.pos):
                            choice = chr(65 + i)
                            break
                    # 如果没有找到点击的选项，使用最后一次的选择
                    if not choice and hasattr(self, 'last_choice'):
                        choice = self.last_choice
                    # 更新反馈文本
                    if choice:
                        self.current_feedback = self.story_manager.get_feedback_text(choice, self.current_language)
                return
                
            if self.state == STATE_MENU:
                self.handle_menu_click(event.pos)
            elif self.state == STATE_INTRO:
                self.handle_intro_click(event.pos)
            elif self.state == STATE_STORY:
                self.handle_story_click(event.pos)
            elif self.state == STATE_CHOICE:
                self.handle_choice_click(event.pos)
            elif self.state == STATE_FEEDBACK:
                self.handle_feedback_click(event.pos)
                
    def update(self):
        if self.current_day > 7 or self.p_value >= 100:
            self.state = STATE_RESULT
            return
            
        # 只要时间在运行就更新时间
        if self.time_running:
            current_real_time = pygame.time.get_ticks() // 1000
            if self.time_start_tick is not None:
                # 更新游戏时间（1秒 = 1分钟）
                elapsed_seconds = current_real_time - self.time_start_tick
                self.current_time = self.game_time + elapsed_seconds
                
                # 只在选项状态且未确认选择时增加P值
                if self.state == STATE_CHOICE and self.p_value_active:
                    if self.last_p_value_update is not None:
                        seconds_since_last_update = current_real_time - self.last_p_value_update
                        if seconds_since_last_update >= self.time_pressure_interval:
                            # 保存当前P值用于比较
                            self.last_p_value = self.p_value
                            self.p_value += self.time_pressure_penalty
                            self.p_value = min(100, self.p_value)
                            # 更新头像状态
                            self.update_student_avatar()
                            
                            self.last_p_value_update = current_real_time
                            print(f"增加P值：当前P值={self.p_value}")  # 调试信息
                
    def draw(self):
        # 清除屏幕
        self.screen.fill(WHITE)
        
        # 根据状态绘制不同的界面
        if self.state == STATE_MENU:
            self.ui_manager.draw_menu()
        elif self.state == STATE_INTRO:
            story_text = self.story_manager.get_current_story()
            print(f"绘制INTRO，文本：{story_text}")  # 调试信息
            self.ui_manager.draw_intro(story_text)
        elif self.state == STATE_STORY:
            story_text = self.story_manager.get_current_story()
            print(f"绘制STORY，文本：{story_text}")  # 调试信息
            self.ui_manager.draw_story(story_text)
        elif self.state == STATE_CHOICE:
            choices = self.story_manager.get_current_choices()
            print(f"绘制CHOICE，选项数：{len(choices)}")  # 调试信息
            self.ui_manager.draw_choices(choices)
        elif self.state == STATE_FEEDBACK:
            print(f"绘制FEEDBACK，反馈：{self.current_feedback}")  # 调试信息
            self.ui_manager.draw_feedback(self.current_feedback)
        elif self.state == STATE_RESULT:
            self.ui_manager.draw_game_over()
            
    def handle_menu_click(self, pos):
        if self.ui_manager.start_button.is_clicked(pos):
            self.state = STATE_INTRO
            self.ui_manager.play_click_sound()
        elif self.ui_manager.quit_button.is_clicked(pos):
            self.ui_manager.play_click_sound()
            pygame.quit()
            sys.exit()
            
    def handle_story_click(self, pos):
        # 检查点击位置是否在按钮区域内
        button_rect = pygame.Rect(1170, 634, 37, 20)  # 使用定的按钮位置和大小
        if button_rect.collidepoint(pos):
            self.ui_manager.play_click_sound()
            print(f"当前状态: {self.state}")
            if self.state == STATE_INTRO:
                print("从INTRO转到STORY")
                self.story_manager.current_phase = "story"
                self.state = STATE_STORY
            elif self.state == STATE_STORY:
                print("从STORY转到CHOICE")
                self.state = STATE_CHOICE
                self.time_running = True
                self.p_value_active = True
                self.time_start_tick = pygame.time.get_ticks() // 1000
                self.last_p_value_update = self.time_start_tick
                
    def handle_choice_click(self, pos):
        # 处理选项点击
        for i, button in enumerate(self.ui_manager.choice_buttons):
            if button.is_clicked(pos):
                self.selected_choice = i
                self.preview_choice = self.story_manager.get_current_choices()[i]
                self.ui_manager.play_choice_click_sound()
                return

        # 处理确认按钮点击
        button_rect = pygame.Rect(1170, 634, 37, 20)  # 使用固定的按钮位置和大小
        if self.selected_choice is not None and button_rect.collidepoint(pos):
            choice = chr(65 + self.selected_choice)
            # 保存最后一次的选择，用于语言切换
            self.last_choice = choice
            
            feedback = self.story_manager.get_current_feedback()[choice]
            # 保存当前P值用于比较
            self.last_p_value = self.p_value
            self.p_value += feedback["p_change"]
            self.p_value = max(0, min(100, self.p_value))
            # 更新学生头像状态
            self.update_student_avatar()
            
            # 获取当前选择的文本（根据当前语言）
            choices = self.story_manager.get_current_choices()
            self.current_choice = choices[self.selected_choice]
            
            # 获取反馈文本（根据当前语言）
            self.current_feedback = self.story_manager.get_feedback_text(choice, self.ui_manager.current_language)
            
            self.state = STATE_FEEDBACK
            self.selected_choice = None
            self.preview_choice = None
            self.ui_manager.play_click_sound()
                
    def handle_feedback_click(self, pos):
        button_rect = pygame.Rect(1170, 634, 37, 20)  # 使用固定的按钮位置和大小
        if button_rect.collidepoint(pos):
            self.ui_manager.play_click_sound()
            self.current_day += 1
            self.story_manager.current_day = self.current_day
            
            # 重置学生状态为normal，除非P值超过80
            if self.p_value >= 80:
                self.student_avatar_state = "over80"
            else:
                self.student_avatar_state = "normal"
            
            if self.current_day <= 7 and self.p_value < 100:
                self.story_manager.current_phase = "intro"
                self.state = STATE_INTRO
                self.generate_game_time()
                self.time_running = False
            else:
                self.state = STATE_RESULT
                
    def handle_intro_click(self, pos):
        if hasattr(self.ui_manager, 'continue_button') and self.ui_manager.continue_button.is_clicked(pos):
            self.ui_manager.play_click_sound()
            if self.state == STATE_INTRO:
                self.story_manager.current_phase = "story"
                self.state = STATE_STORY
        
    def draw_teacher_text(self, text):
        if not text:
            return
        
        font = pygame.font.Font(None, 20)  # 减小字体大小以适应英文文本
        
        # 计算每行最大字符数
        max_chars_per_line = self.teacher_text_bounds['width'] // 10  # 估计每个字符的平均宽度
        
        # 分行处理文本
        words = text.split()
        lines = []
        current_line = []
        current_line_length = 0
        
        for word in words:
            # 测试添加这个词后的宽度
            test_line = ' '.join(current_line + [word])
            test_surface = font.render(test_line, True, (0, 0, 0))
            
            if test_surface.get_width() <= self.teacher_text_bounds['width']:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                    current_line = [word]
                else:
                    # 如果单词太长，强制分割
                    while word:
                        for i in range(len(word), 0, -1):
                            part = word[:i]
                            part_surface = font.render(part, True, (0, 0, 0))
                            if part_surface.get_width() <= self.teacher_text_bounds['width']:
                                lines.append(part)
                                word = word[i:]
                                break
        
        if current_line:
            lines.append(' '.join(current_line))
        
        # 控制显示行数，避免超出边界
        line_height = font.get_linesize()
        max_lines = self.teacher_text_bounds['height'] // line_height
        lines = lines[:max_lines]
        
        # 绘制文本
        y = self.teacher_text_bounds['top']
        for line in lines:
            text_surface = font.render(line, True, (0, 0, 0))
            x = self.teacher_text_bounds['left']
            self.screen.blit(text_surface, (x, y))
            y += line_height
        
    def create_buttons(self):
        """创建所有按钮"""
        # 开始游戏按钮
        start_button_rect = pygame.Rect(400, 300, 200, 50)
        self.start_button = Button(rect=start_button_rect, color=None)
        self.start_button.text = "开始游戏" if self.current_language == LANGUAGE_CN else "Start Game"
        
        # 结束游戏按钮
        end_button_rect = pygame.Rect(400, 400, 200, 50)
        self.end_button = Button(rect=end_button_rect, color=None)
        self.end_button.text = "结束游戏" if self.current_language == LANGUAGE_CN else "End Game"
        
        # 语言切换按钮
        lang_button_rect = pygame.Rect(700, 50, 100, 40)
        self.language_button = Button(rect=lang_button_rect, color=None)
        self.language_button.text = "English" if self.current_language == LANGUAGE_CN else "中文"
        
        # 继续按钮
        continue_button_rect = pygame.Rect(1170, 634, 37, 20)
        self.continue_button = Button(rect=continue_button_rect, color=None)
        self.continue_button.text = "继续" if self.current_language == LANGUAGE_CN else "Continue"

    def switch_language(self):
        """切换语言"""
        self.current_language = LANGUAGE_EN if self.current_language == LANGUAGE_CN else LANGUAGE_CN
        # 强制更新所有按钮文本
        self.create_buttons()

    def start_game(self):
        """开始游戏"""
        self.game_started = True
        
    def end_game(self):
        """结束游戏"""
        pygame.quit()
        exit()
        
    def continue_game(self):
        """继续游戏"""
        # 处理继续游戏的逻辑...
        pass
        
    def update_student_avatar(self):
        """根据P值变化更新学生头像状态"""
        old_state = self.student_avatar_state
        
        # 如果P值超过80，优先显示over80状态
        if self.p_value >= 80:
            self.student_avatar_state = "over80"
        # 否则根据P值变化显示up或down状态
        elif self.p_value > self.last_p_value:
            self.student_avatar_state = "up"
        elif self.p_value < self.last_p_value:
            self.student_avatar_state = "down"
        else:
            self.student_avatar_state = "normal"
        
        if old_state != self.student_avatar_state:
            print(f"头像状态变化: {old_state} -> {self.student_avatar_state}, P值: {self.p_value}, 上次P值: {self.last_p_value}")  # 添加更详细的调试信息