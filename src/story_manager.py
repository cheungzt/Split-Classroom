import pygame
from constants import LANGUAGE_CN, LANGUAGE_EN
from story_data import get_stories

class StoryManager:
    def __init__(self):
        self.current_day = 1
        self.current_phase = "intro"
        
        # 基础UI文本
        self.ui_text = {
            "start_game": {
                LANGUAGE_CN: "开始游戏",
                LANGUAGE_EN: "Start Game"
            },
            "end_game": {
                LANGUAGE_CN: "结束游戏",
                LANGUAGE_EN: "End Game"
            },
            "continue": {
                LANGUAGE_CN: "继续",
                LANGUAGE_EN: "Continue"
            },
            "back": {
                LANGUAGE_CN: "返回",
                LANGUAGE_EN: "Back"
            },
            "switch_language": {
                LANGUAGE_CN: "English",
                LANGUAGE_EN: "中文"
            },
            "narrative_title": {
                LANGUAGE_CN: "开场叙事",
                LANGUAGE_EN: "Opening Narrative"
            },
            "inner_monologue": {
                LANGUAGE_CN: "内心独白",
                LANGUAGE_EN: "Inner Monologue"
            },
            "phone_message": {
                LANGUAGE_CN: "手机信息",
                LANGUAGE_EN: "Phone Message"
            }
        }
        
        # 教师反馈文本
        self.feedback = {
            LANGUAGE_CN: [
                "很好，你正在逐渐适应课堂环境。继续保持这种态度，慢慢来，不要给自己太大压力。",
                "你今天的表现让我很欣慰。记住，每个人都有不同的学习节奏，重要的是持续进步。",
                "我能感受到你在努力克服困难。相信自己，你已经比以前进步很多了。",
                "看到你愿意尝试回答问题，这是很大的突破。不要害怕犯错，这是学习过程的一部分。",
                "你的进步我都看在眼里。继续保持这种学习态度，我相信你一定会越来越好的。"
            ],
            LANGUAGE_EN: [
                "Good job, you're gradually adapting to the classroom environment. Keep up this attitude, take it slow, and don't put too much pressure on yourself.",
                "Your performance today makes me very pleased. Remember, everyone has their own learning pace, what matters is continuous improvement.",
                "I can feel your effort in overcoming difficulties. Trust yourself, you've made a lot of progress compared to before.",
                "Seeing you willing to try answering questions is a big breakthrough. Don't be afraid of making mistakes, it's part of the learning process.",
                "I've noticed all your progress. Keep maintaining this learning attitude, and I believe you'll keep getting better."
            ]
        }
        
        # 加载故事内容
        self.stories = get_stories()
    
    def get_ui_text(self, key, language):
        """获取UI文本"""
        return self.ui_text.get(key, {}).get(language, "")
    
    def get_feedback(self, index, language):
        """获取反馈文本"""
        if 0 <= index < len(self.feedback.get(language, [])):
            return self.feedback[language][index]
        return ""
    
    def get_current_story(self):
        """获取当前故事内容"""
        if self.current_day in self.stories:
            if self.current_phase == "intro":
                return self.stories[self.current_day]["intro"]
            return self.stories[self.current_day]["story"]
        return ""
    
    def get_current_choices(self):
        """获取当前选项"""
        if self.current_day in self.stories:
            return self.stories[self.current_day]["choices"]
        return []
    
    def get_current_feedback(self):
        """获取当前反馈"""
        if self.current_day in self.stories:
            return self.stories[self.current_day].get("feedback", {})
        return {}

    def get_choice_feedback(self, choice_key):
        """获取特定选项的反馈"""
        feedback = self.get_current_feedback()
        return feedback.get(choice_key, {})

    def get_feedback_text(self, choice_key, language):
        """获取反馈文本
        Args:
            choice_key: 选项键值（如 'A', 'B', 'C'）
            language: 语言（LANGUAGE_CN 或 LANGUAGE_EN）
        Returns:
            str: 对应语言的反馈文本
        """
        try:
            # 获取当前天的反馈
            current_story = self.stories.get(self.current_day, {})
            feedback = current_story.get("feedback", {})
            
            # 获取特定选项的反馈
            choice_feedback = feedback.get(choice_key, {})
            
            # 获取反馈文本
            text = choice_feedback.get("text", {})
            
            # 确保text是字典类型
            if not isinstance(text, dict):
                print(f"Warning: feedback text for {choice_key} is not a dict")
                return str(text)
                
            # 获取对应语言的文本
            result = text.get(language, "")
            if not result:
                print(f"Warning: no text found for language {language}")
                # 如果找不到对应语言的文本，返回另一种语言的文本
                other_language = LANGUAGE_EN if language == LANGUAGE_CN else LANGUAGE_CN
                result = text.get(other_language, "")
                
            return result
            
        except Exception as e:
            print(f"Error getting feedback text: {e}")
            return ""

    def get_feedback_change(self, choice_key):
        """获取反馈对应的变化值"""
        feedback = self.get_choice_feedback(choice_key)
        if isinstance(feedback, dict) and "p_change" in feedback:
            return feedback["p_change"]
        return 0

    def set_phase(self, phase):
        """设置当前阶段"""
        self.current_phase = phase

    def get_current_time_range(self):
        """获取当前时间范围"""
        if self.current_day in self.stories:
            return self.stories[self.current_day]["time_range"]
        return []

    def advance_day(self):
        """进入下一天"""
        if self.current_day < 7:
            self.current_day += 1
            self.current_phase = "intro"
            return True
        return False

    def get_total_days(self):
        """获取总天数"""
        return len(self.stories)

    def is_last_day(self):
        """检查是否是最后一天"""
        return self.current_day >= self.get_total_days()