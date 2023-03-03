important commands

To get openai whisper
```
pip install git+https://github.com/openai/whisper.git SpeechRecognition
```

Future Scope

Error handling: Add error handling to handle exceptions that may occur during the summarization process.

Multi-language support: Use a language detection library to identify the language of the video and use a speech-to-text library that supports that language.
- [multi-language support](https://huggingface.co/voidful/wav2vec2-xlsr-multilingual-56)
- [multi-language summarization 1](https://huggingface.co/csebuetnlp/mT5_multilingual_XLSum)
- [multi-language summarization 2](https://huggingface.co/csebuetnlp/mT5_m2m_crossSum)
- [multi-language summarization 3](https://huggingface.co/spursyy/mT5_multilingual_XLSum_rust)
- [multi-language summarization 4](https://huggingface.co/csebuetnlp/mT5_m2m_crossSum_enhanced)

Summarization customization: Provide options for the user to customize the summarization process, such as the length of the summary or specific sections of the video to summarize.

Integration with other tools: Integrate your application with other tools or services, such as text-to-speech or cloud-based video hosting platforms.

User interface: Create a graphical user interface (GUI) to make it easier for users to interact with your application.