from constants import LANGUAGE_CN, LANGUAGE_EN

# 定义每天的故事内容
day1 = {
    "intro": {
        LANGUAGE_CN: "周一：开场叙事\n内心独白：昨晚，我梦见自己站在一个讲堂里，所有人都盯着我看。我无法出声，只觉得自己快要崩溃了。今天早上醒来，我依旧感到焦虑不安。今天有Simon老师的管理课，她总是那么温柔，可每次她看着我，我却觉得自己无法应付她的期待。",
        LANGUAGE_EN: "Monday: Opening Narrative\nInner Monologue: Last night, I dreamed of standing in a lecture hall with everyone staring at me. I couldn't make a sound and felt like I was about to break down. Waking up this morning, I still feel anxious and uneasy. Today we have Ms. Simon's management class. She's always so gentle, but whenever she looks at me, I feel like I can't live up to her expectations."
    },
    "story": {
        LANGUAGE_CN: "Simon老师今天讲授的是如何处理学术中的压力和自我管理。他总是以平和的语气与我们分享如何有效沟通和调整情绪，课堂节奏也较为轻松。尽管他的言辞温和，我却觉得自己总是无法做到他所说的那样平静。",
        LANGUAGE_EN: "Simon teacher today teaches how to deal with academic pressure and self-management. He always shares how to effectively communicate and adjust emotions with a gentle tone. Although his words are gentle, I feel like I can't always do what he says."
    },
    "time_range": ["10:30", "12:30", "13:30", "17:30"],
    "choices": [
        {
            LANGUAGE_CN: "A. 听从Simon老师的建议，决定用一小段时间整理自己的情绪，调整状态。",
            LANGUAGE_EN: "A. Follow Simon's advice, take some time to organize emotions and adjust state."
        },
        {
            LANGUAGE_CN: "B. 对Simon老师的建议持怀疑态度，认为这些方法太过理想化，不适用于自己。",
            LANGUAGE_EN: "B. Be skeptical of Simon's advice, thinking these methods are too idealistic and not suitable."
        },
        {
            LANGUAGE_CN: "C. 在课堂上主动发言，尝试分享自己的一些情绪困扰。",
            LANGUAGE_EN: "C. Speak up in class, try to share some emotional troubles."
        }
    ],
    "feedback": {
        "A": {
            "text": {
                LANGUAGE_CN: "Simon老师点了点头，微笑着鼓励你。他看着你整理情绪的��为，似乎稍微松了一口气，但他的眼神依旧带着些许的担忧。",
                LANGUAGE_EN: "Professor Simon nods and smiles encouragingly. Watching you manage your emotions, he seems to relax a little, but his eyes still show a hint of concern."
            },
            "p_change": -5
        },
        "B": {
            "text": {
                LANGUAGE_CN: "Simon老师似乎察觉到了你的怀疑，他的语气柔和却有些犹豫，显然希望你能够更信任他的建议。",
                LANGUAGE_EN: "Professor Simon seems to notice your skepticism, his tone gentle but hesitant, clearly hoping you would trust his advice more."
            },
            "p_change": 10
        },
        "C": {
            "text": {
                LANGUAGE_CN: "你主动发言，Simon老师轻轻地点了点头，赞许你的勇气，但他的眼中却露出了一丝不易察觉的担心，似乎对你的情绪波动感到不安。",
                LANGUAGE_EN: "You speak up voluntarily, and Professor Simon gently nods, appreciating your courage, but his eyes reveal a subtle worry, seemingly concerned about your emotional fluctuations."
            },
            "p_change": 15
        }
    }
}

day2 = {
    "intro": {
        LANGUAGE_CN: "周二：开场叙事\n手机信息：今天早上收到Anthony老师的邮件，他说我们今天的理论课将讨论一些复杂的概念，要求我们做出独立的思考。我有些焦虑，因为我总觉得自己没能完全理解他的课程内容，怕上课时被揭穿。",
        LANGUAGE_EN: "Tuesday: Opening Narrative\nPhone Message: This morning I received an email from Professor Anthony saying that today's theory class will discuss some complex concepts and require independent thinking. I'm anxious because I always feel like I haven't fully understood his course content and fear being exposed in class."
    },
    "story": {
        LANGUAGE_CN: "Anthony老师今天讲授了一些复杂的理论内容，他总是通过幽默的方式化解难题，课堂气氛轻松而富有挑战。大家在讨论中时不时地会笑出声，Anthony老师的轻松气氛让你一方面感到放松，但另一方面又担心自己跟不上。",
        LANGUAGE_EN: "Professor Anthony taught some complex theoretical content today. He always solves difficult problems with humor, making the classroom atmosphere relaxed yet challenging. Everyone laughs occasionally during discussions. Anthony's casual atmosphere makes you feel relaxed on one hand, but worried about keeping up on the other."
    },
    "time_range": ["9:30", "11:30", "12:30", "18:30"],
    "choices": [
        {
            LANGUAGE_CN: "A. 尝试积极参与课堂讨论，即使不完全理解，也尽量表达自己的想法。",
            LANGUAGE_EN: "A. Try to actively participate in class discussions and express your thoughts even if you don't fully understand."
        },
        {
            LANGUAGE_CN: "B. 由于害怕出错，选择尽量保持沉默，避免暴露自己的不足。",
            LANGUAGE_EN: "B. Choose to stay silent due to fear of making mistakes, avoiding exposing your shortcomings."
        },
        {
            LANGUAGE_CN: "C. 觉得这门课不值得花太多时间投入，选择忽略课堂内容，专心做自己的事。",
            LANGUAGE_EN: "C. Feel this course isn't worth investing too much time in, choose to ignore class content and focus on your own things."
        }
    ],
    "feedback": {
        "A": {
            "text": {
                LANGUAGE_CN: "Anthony老师微笑着看向你，他鼓励你继续发言，尽管你的观点可能不完整，但他的眼神中流露出一丝赞许。这种轻松的反馈让你略感安心。",
                LANGUAGE_EN: "Professor Anthony smiles at you, encouraging you to continue speaking. Although your points might not be complete, his eyes show a hint of approval. This relaxed feedback makes you feel somewhat at ease."
            },
            "p_change": 15
        },
        "B": {
            "text": {
                LANGUAGE_CN: "Anthony老师在课堂上看向你，你感到他并没有明显的批评，但他的目光让你更加羞愧，你选择沉默，避免暴露自己的不足。",
                LANGUAGE_EN: "Professor Anthony looks at you in class. While there's no obvious criticism, his gaze makes you feel more ashamed, leading you to choose silence to avoid exposing your inadequacies."
            },
            "p_change": 10
        },
        "C": {
            "text": {
                LANGUAGE_CN: "你感到这门课并不重要，于是选择忽略课程内容，专心做自己的事。Anthony老师似乎有些疑惑地看了你一眼，虽然没说什么，但他的目光中带着些许失望。",
                LANGUAGE_EN: "Feeling this course isn't important, you choose to ignore the content and focus on your own things. Professor Anthony glances at you with confusion, and though he doesn't say anything, his eyes carry a hint of disappointment."
            },
            "p_change": -5
        }
    }
}

day3 = {
    "intro": {
        LANGUAGE_CN: "周三：开场叙事\n内心独白：昨天的课程让我感到有些不安，今天还要面对David老师的商业课。他总是那么严格，���不知道自己能否应付得来。",
        LANGUAGE_EN: "Wednesday: Opening Narrative\nInner Monologue: Yesterday's class made me feel a bit uneasy. Today I have to face Professor David's business class. He's always so strict, I don't know if I can handle it."
    },
    "story": {
        LANGUAGE_CN: "David老师非常严格，课堂上气氛紧张，课件和案例分析都非常具挑战性。他要求大家尽快回答问题，如果有人回答不及时，甚至会直接表示不满。今天，你似乎没能及时回答一个问题，David老师的脸上露出了明显的不悦。",
        LANGUAGE_EN: "Professor David is very strict, the classroom atmosphere is tense, and the courseware and case analyses are very challenging. He requires everyone to answer questions quickly, and if someone doesn't respond in time, he will directly express his dissatisfaction. Today, you seemed unable to answer a question promptly, and Professor David showed obvious displeasure."
    },
    "time_range": ["13:30", "17:30"],
    "choices": [
        {
            LANGUAGE_CN: "A. 认真思考问题，努力做到尽量完美，避免被批评。",
            LANGUAGE_EN: "A. Think carefully about the problem and try to be as perfect as possible to avoid criticism."
        },
        {
            LANGUAGE_CN: "B. 感到自己已经尽力了，决定不再过分焦虑，尽量平和面对。",
            LANGUAGE_EN: "B. Feel that you've done your best, decide not to be overly anxious, and try to face it calmly."
        },
        {
            LANGUAGE_CN: "C. 直接反驳David老师，觉得他的批评不公，挑战他。",
            LANGUAGE_EN: "C. Directly confront Professor David, feeling his criticism is unfair, and challenge him."
        }
    ],
    "feedback": {
        "A": {
            "text": {
                LANGUAGE_CN: "David老师看着你，似乎期待你回答得更快。你回答了问题，但David老师的眼神没有明显的赞赏，反而显得更为严厉。",
                LANGUAGE_EN: "Professor David watches you, seemingly expecting a quicker response. You answer the question, but instead of showing obvious approval, his expression becomes even more stern."
            },
            "p_change": 15
        },
        "B": {
            "text": {
                LANGUAGE_CN: "David老师冷冷地看了你一眼，似乎对你的消极态度并不满意。他并未做出进一步的评论，你感到更加强烈的不安。",
                LANGUAGE_EN: "Professor David gives you a cold look, seemingly dissatisfied with your passive attitude. He makes no further comment, leaving you feeling increasingly uneasy."
            },
            "p_change": -5
        },
        "C": {
            "text": {
                LANGUAGE_CN: "David老师的严厉态度引发了你的反抗，你直接反驳了他，课堂的气氛一下变得紧张。David老师没有说话，但他那冷峻的目光让你有些不安。",
                LANGUAGE_EN: "Professor David's strict attitude provokes your defiance, and you directly confront him, instantly making the classroom atmosphere tense. Professor David remains silent, but his stern gaze makes you feel uncomfortable."
            },
            "p_change": 20
        }
    }
}

day4 = {
    "intro": {
        LANGUAGE_CN: "周四：开场叙事\n内心独白：昨天我因为David老师的严厉批评情绪失控了，感觉自己好像在课堂上暴露了所有的不安。今天早上，我在想着，或许该开始认真做一些技术类的工作，换个方式释放压力。",
        LANGUAGE_EN: "Thursday: Opening Narrative\nInner Monologue: Yesterday I lost control of my emotions due to Professor David's harsh criticism, feeling like I exposed all my insecurities in class. This morning, I'm thinking maybe I should start doing some technical work seriously, finding a different way to release pressure."
    },
    "story": {
        LANGUAGE_CN: "Gio老师带我们进行了一次技术性的实操，要求我们独立完成问题分析。课堂气氛严谨却不压抑，他鼓励我们挑战自我，解决实际问题。虽然有些困难，但他并没有给我们很大压力，而是根据进展给出指导。",
        LANGUAGE_EN: "Professor Gio led us through a technical hands-on session, requiring us to complete problem analysis independently. The classroom atmosphere was rigorous but not oppressive. He encouraged us to challenge ourselves and solve practical problems. Although it was somewhat difficult, he didn't put much pressure on us, instead providing guidance based on our progress."
    },
    "time_range": ["9:30", "11:30", "12:30", "18:30"],
    "choices": [
        {
            LANGUAGE_CN: "A. 坚持解决技术难题，逐步克服困惑。",
            LANGUAGE_EN: "A. Persist in solving technical problems, gradually overcoming confusion."
        },
        {
            LANGUAGE_CN: "B. 觉得自己可能做不出来，选择放弃一部分任务。",
            LANGUAGE_EN: "B. Feel that you might not be able to complete it, choose to give up part of the task."
        },
        {
            LANGUAGE_CN: "C. 故意做出一些不完全的答案，看看Gio老师的反应。",
            LANGUAGE_EN: "C. Deliberately give some incomplete answers to see Professor Gio's reaction."
        }
    ],
    "feedback": {
        "A": {
            "text": {
                LANGUAGE_CN: "Gio老师微微点头，给予了一些积极的反馈，但他并没有过度鼓励。你感到自己还需要付出更多的努力。",
                LANGUAGE_EN: "Professor Gio nods slightly, offering some positive feedback, but without excessive encouragement. You feel you need to put in more effort."
            },
            "p_change": -5
        },
        "B": {
            "text": {
                LANGUAGE_CN: "Gio老师稍微皱了皱眉，对你放弃任务的决定表示了些许失望。",
                LANGUAGE_EN: "Professor Gio frowns slightly, showing some disappointment at your decision to give up part of the task."
            },
            "p_change": 10
        },
        "C": {
            "text": {
                LANGUAGE_CN: "你故意做出不完全的答案，Gio老师显然注意到并微微皱眉，但他没有直接批评，只是简短地提醒你下次要更加专注。",
                LANGUAGE_EN: "You deliberately give incomplete answers, and Professor Gio clearly notices and frowns slightly, but instead of direct criticism, he briefly reminds you to be more focused next time."
            },
            "p_change": 15
        }
    }
}

day5 = {
    "intro": {
        LANGUAGE_CN: "周五：开场叙事\n手机信息：今天导师发了一条信息，提醒我明天有个关于论文进度的讨论会。我感到非常紧张，觉得自己似乎没有做到他期待的那样。我真希望自己能放松，但一想到讨论会，我的心就乱了。",
        LANGUAGE_EN: "Friday: Opening Narrative\nPhone Message: Today my supervisor sent a message reminding me of tomorrow's thesis progress discussion. I feel very nervous, thinking I haven't met his expectations. I really wish I could relax, but just thinking about the discussion makes my heart race."
    },
    "story": {
        LANGUAGE_CN: "今天下午，Henry导师约你去他的办公室讨论论文进度。你知道，导师对你的学术进展非常关注，但你一直觉得自己做得不够好。你不知道是否应该向导师坦白自己目前的困境，还是尝试表现出更为成熟的一面。",
        LANGUAGE_EN: "This afternoon, Professor Henry invited you to his office to discuss your thesis progress. You know that your supervisor is very concerned about your academic progress, but you've always felt that you're not doing well enough. You're unsure whether to be honest with him about your current difficulties or try to appear more mature."
    },
    "time_range": ["9:30", "17:30"],
    "choices": [
        {
            LANGUAGE_CN: "A. 诚实地告诉导师你目前的困境和焦虑，希望得到更多的指导。",
            LANGUAGE_EN: "A. Honestly tell your supervisor about your current difficulties and anxieties, hoping for more guidance."
        },
        {
            LANGUAGE_CN: "B. 表现得自信一些，尽量掩饰自己的困境，表现出自己的独立性。",
            LANGUAGE_EN: "B. Act more confident, try to hide your difficulties, and show your independence."
        },
        {
            LANGUAGE_CN: "C. 避免谈论自己的情绪和困惑，尽量集中讨论论文内容。",
            LANGUAGE_EN: "C. Avoid discussing your emotions and confusion, try to focus on the thesis content."
        }
    ],
    "feedback": {
        "A": {
            "text": {
                LANGUAGE_CN: "Henry导师皱了皱眉，沉思了一会儿，然后安慰你说学术的压力是常有的事，并给出了具体的改进建议。他的语气温和，但你能感到他有些担忧。",
                LANGUAGE_EN: "Professor Henry furrows his brow, contemplates for a moment, then comforts you saying academic pressure is common, and offers specific suggestions for improvement. His tone is gentle, but you can sense his concern."
            },
            "p_change": -10
        },
        "B": {
            "text": {
                LANGUAGE_CN: "Henry导师看着你，似乎有些犹豫，但并未过多表示。他轻描淡写地讨论了你的进展，看起来你成功掩饰了自己的焦虑。",
                LANGUAGE_EN: "Professor Henry looks at you, seeming somewhat hesitant, but doesn't say much. He discusses your progress casually, and it appears you've successfully hidden your anxiety."
            },
            "p_change": 10
        },
        "C": {
            "text": {
                LANGUAGE_CN: "Henry导师专注于论文的具体内容，没有过多关注你的情绪。他表扬了你的工作，但你心里却有种被忽略的感觉。",
                LANGUAGE_EN: "Professor Henry focuses on the specific content of the thesis, without paying much attention to your emotions. He praises your work, but you feel somewhat overlooked inside."
            },
            "p_change": 15
        }
    }
}

day6 = {
    "intro": {
        LANGUAGE_CN: "周六：开场叙事\n手机信息：今天早上，我收到了一条来自Simon老师的消息。他提醒我今天要做些轻松的事情，毕竟下周的课程内容不那么复杂。但我仍然感到心里有些不安，总觉得自己没准备好。",
        LANGUAGE_EN: "Saturday: Opening Narrative\nPhone Message: This morning, I received a message from Professor Simon. He reminded me to do something relaxing today, since next week's course content isn't too complex. But I still feel uneasy, always feeling like I'm not prepared enough."
    },
    "story": {
        LANGUAGE_CN: "今天你在图书馆碰到Simon老师，他似乎刚刚做完一次小组指导，正在整理一些笔记。看到你，他微笑着打招呼，随后谈起了自己如何调整情绪来应对工作中的压力。他提到,'面对挑战时,保持冷静和理智很重要,但也需要给自己一些宽容。'",
        LANGUAGE_EN: "Today you met Professor Simon in the library. He seemed to have just finished a group tutorial and was organizing some notes. Seeing you, he smiled and greeted you, then talked about how he adjusts his emotions to deal with work pressure. He mentioned, 'When facing challenges, it's important to stay calm and rational, but also to give yourself some tolerance.'"
    },
    "time_range": ["9:30", "17:30"],
    "choices": [
        {
            LANGUAGE_CN: "A. 听从Simon老师的建议，决定尝试放慢节奏，给自己一些空间，先做一些轻松的事情。",
            LANGUAGE_EN: "A. Follow Professor Simon's advice, decide to slow down, give yourself some space, and do something relaxing first."
        },
        {
            LANGUAGE_CN: "B. 感到自己还不能放松，继续告诉自己要全力以赴，尽量避免让自己休息。",
            LANGUAGE_EN: "B. Feel that you can't relax yet, continue to tell yourself to give it your all, try to avoid taking a rest."
        },
        {
            LANGUAGE_CN: "C. 与Simon老师深入交流，谈谈自己对情绪管理的困惑，寻求他更多的建议。",
            LANGUAGE_EN: "C. Have an in-depth conversation with Professor Simon about your confusion regarding emotional management, seeking more advice from him."
        }
    ],
    "feedback": {
        "A": {
            "text": {
                LANGUAGE_CN: "Simon老师听完你的决定后，温柔地笑了笑，说：'有时候休息和放松确实很重要，但也要确保自己有足够的动力。'他似乎对你这种逐渐放松的态度感到欣慰。",
                LANGUAGE_EN: "After hearing your decision, Professor Simon smiles gently and says, 'Sometimes rest and relaxation are indeed important, but make sure you maintain enough motivation.' He seems pleased with your gradually relaxing attitude."
            },
            "p_change": -5
        },
        "B": {
            "text": {
                LANGUAGE_CN: "Simon老师点了点头，表示理解你的坚持，但他提醒你：'过度焦虑往往只会适得其反，试着找个平衡。'你心里有些不安，似乎无法完全放下心中的焦虑。",
                LANGUAGE_EN: "Professor Simon nods, showing understanding of your persistence, but reminds you: 'Excessive anxiety often becomes counterproductive, try to find a balance.' You feel somewhat uneasy, unable to fully let go of your anxiety."
            },
            "p_change": 5
        },
        "C": {
            "text": {
                LANGUAGE_CN: "你向Simon老师分享了自己的一些困惑，他耐心地听完并给出了一些理性建议，鼓励你学会为自己设定合理的目标，并且在压力过大时寻求外部支持。",
                LANGUAGE_EN: "You share your confusion with Professor Simon, who listens patiently and offers some rational advice, encouraging you to learn to set reasonable goals for yourself and seek external support when pressure becomes too much."
            },
            "p_change": 10
        }
    }
}

day7 = {
    "intro": {
        LANGUAGE_CN: "周日：开场叙事\n内心独白：今天早上，我又收到了David老师的消息，他提醒我们要预习下周的案例分析。我知道这次任务很重要，但心里又感到有些不安。上次在课堂上，我没有及时回答问题，今天我更怕自己再次被批评。",
        LANGUAGE_EN: "Sunday: Opening Narrative\nInner Monologue: This morning, I received another message from Professor David, reminding us to preview next week's case analysis. I know this task is important, but I feel uneasy again. Last time in class, I didn't answer questions promptly, and today I'm more afraid of being criticized again."
    },
    "story": {
        LANGUAGE_CN: "你在周日下午遇到David老师，他正在咖啡厅里看一些商业杂志。看到你，他邀请你坐下来喝杯咖啡。谈话中，David老师提到他在自己职业生涯中的一段经历，讲述了如何在商业决策中面对巨大的压力，并强调了'只有快速决策，才能在竞争中脱颖而出'。你感到很受触动，虽然他的故事很鼓舞人心，但你仍然害怕自己会做出错误的决策。",
        LANGUAGE_EN: "You met Professor David on Sunday afternoon, who was reading some business magazines in a cafe. Seeing you, he invited you to sit down for a coffee. During the conversation, Professor David mentioned an experience from his career, describing how he faced enormous pressure in business decisions, emphasizing that 'only quick decisions can help you stand out in competition.' You feel moved, although his story is inspiring, you're still afraid of making wrong decisions."
    },
    "time_range": ["9:30", "17:30"],
    "choices": [
        {
            LANGUAGE_CN: "A. 表示赞同David老师的观点，并试图自己在工作中进行更多决策，以提升自信。",
            LANGUAGE_EN: "A. Agree with Professor David's view and try to make more decisions in your work to build confidence."
        },
        {
            LANGUAGE_CN: "B. 感到自己的能力还不足以做出决策，决定继续观察，避免做出任何过于冒险的选择。",
            LANGUAGE_EN: "B. Feel that your abilities are not yet sufficient to make decisions, decide to continue observing, avoid making any overly risky choices."
        },
        {
            LANGUAGE_CN: "C. 向David老师提出自己对做决策的疑虑，询问他如何更好地判断是否该冒险。",
            LANGUAGE_EN: "C. Express your concerns about decision-making to Professor David, ask him how to better judge whether to take risks."
        }
    ],
    "feedback": {
        "A": {
            "text": {
                LANGUAGE_CN: "David老师听完后点了点头：'不错，做出决策是成功的关键，但你得确保你的每一步都经过深思熟虑。'他的话语既鼓励又不失严谨。",
                LANGUAGE_EN: "Professor David nods after listening: 'Good, making decisions is key to success, but you must ensure each step is well thought out.' His words are both encouraging and rigorous."
            },
            "p_change": 5
        },
        "B": {
            "text": {
                LANGUAGE_CN: "David老师没有表现出不满，只是平静地回应：'观察是很重要的，但如果你总是等着完美的时机，可能会错失良机。'你感到自己有些被动，仍未完全敢于面对挑战。",
                LANGUAGE_EN: "Professor David shows no dissatisfaction, just calmly responds: 'Observation is important, but if you always wait for the perfect moment, you might miss opportunities.' You feel somewhat passive, still not fully ready to face challenges."
            },
            "p_change": -5
        },
        "C": {
            "text": {
                LANGUAGE_CN: "David老师认真听你讲述后，给出了���具建设性的反馈，他建议你将大局观和细节结合起来，才可能做出最佳决策。你感到自己从中获得了一些启发。",
                LANGUAGE_EN: "After listening to you carefully, Professor David provides more constructive feedback, suggesting that combining both the big picture and details is necessary for making the best decisions. You feel you've gained some insight from this."
            },
            "p_change": 10
        }
    }
}

# 将所有天的内容组合成字典
stories = {
    1: day1,
    2: day2,
    3: day3,
    4: day4,
    5: day5,
    6: day6,
    7: day7
}

def get_stories():
    return stories 