struct ChatBubbleView: View {
    @ObservedObject var viewModel: ChatViewModel
    let message: Message
    @State private var isTranslated = false
    
    var body: some View {
        HStack {
            if message.isFromTeacher {
                Spacer()
                VStack(alignment: .trailing) {
                    ScrollView(.vertical, showsIndicators: true) {
                        Text(isTranslated ? message.translatedText ?? message.text : message.text)
                            .font(.system(size: 14))
                            .lineSpacing(4)
                            .padding(12)
                            .multilineTextAlignment(.leading)
                            .frame(width: 330, alignment: .leading)
                    }
                    .frame(width: 350, height: 269)
                    .background(Color.blue.opacity(0.2))
                    .cornerRadius(10)
                    .position(x: 857, y: 359)
                    .onTapGesture {
                        isTranslated.toggle()
                    }
                }
            } else {
                VStack(alignment: .leading) {
                    Text(isTranslated ? message.translatedText ?? message.text : message.text)
                        .padding()
                        .background(Color.gray.opacity(0.2))
                        .cornerRadius(10)
                        .onTapGesture {
                            isTranslated.toggle()
                        }
                }
                Spacer()
            }
        }
        .padding(.horizontal)
    }
} 