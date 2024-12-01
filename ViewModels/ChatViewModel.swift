class ChatViewModel: ObservableObject {
    @Published var messages: [Message] = []
    private let translator: TranslationService
    
    init(translator: TranslationService = TranslationService()) {
        self.translator = translator
    }
    
    func translateMessage(_ message: Message) async -> Bool? {
        guard let index = messages.firstIndex(where: { $0.id == message.id }) else { return nil }
        
        do {
            guard !message.text.isEmpty else { return nil }
            
            let translatedText = try await translator.translate(message.text)
            
            guard !translatedText.isEmpty, translatedText != message.text else { return nil }
            
            await MainActor.run {
                self.messages[index].translatedText = translatedText
            }
            return true
            
        } catch {
            print("Translation error: \(error.localizedDescription)")
            return nil
        }
    }
} 