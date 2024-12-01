struct Message: Identifiable {
    let id: UUID
    let text: String
    var translatedText: String?
    let isFromTeacher: Bool
    
    init(id: UUID = UUID(), text: String, isFromTeacher: Bool) {
        self.id = id
        self.text = text
        self.isFromTeacher = isFromTeacher
    }
} 