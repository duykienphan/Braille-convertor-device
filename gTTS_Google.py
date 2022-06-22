from gtts import gTTS #need internet connection
import os
from playsound import playsound #use playsound==1.2.2 package

def speak(text):
    i = 0
    tts = gTTS(text=text, tld='com.vn', lang='vi')
    os.remove("D:/Kien Phan/Projects/Text to speech - Python/voice.mp3")
    filename = "voice.mp3"
    tts.save(filename)
    playsound(filename)

#main code
word = ""
text = ""

tone_marks = ["<", ">", "?", "~", "."] #sắc, huyền, hỏi, ngã, nặng

braille_encode = ['1', ' ', ' ', ' ', ' ', ' ', '345', ' ', ' ', ' ', ' ', ' ', '16', ' ', ' ', ' ', ' ', ' ', '12', '14', '145', '2346',
                '15', ' ', ' ', ' ', ' ', ' ', '126', ' ', ' ', ' ', ' ', ' ', '124', '1245', '125', '24', ' ', ' ', ' ', ' ', ' ', '245', '13', 
                '123', '134', '1345', '135', ' ', ' ', ' ', ' ', ' ', '1456', ' ', ' ', ' ', ' ', ' ', '246', ' ', ' ', ' ', ' ', ' ', '1234', '12345',
                '1235', '234', '2345', '136',  ' ', ' ', ' ', ' ', ' ','1256', ' ', ' ', ' ', ' ', ' ', '1236', '2456', '1346', '13456', ' ', ' ', ' ', ' ', ' ', '1356']

tone_marks_encode = ['35', '56', '26', '36', '6']
                
alphabet = ['a', 'à', 'ả', 'ã', 'á', 'ạ', 'ă', 'ằ', 'ẳ', 'ẵ', 'ắ', 'ặ', 'â', 'ầ', 'ẩ', 'ẫ', 'ấ', 'ậ', 'b', 'c', 'd', 'đ', 
        'e', 'è', 'ẻ', 'ẽ', 'é', 'ẹ', 'ê', 'ề', 'ể', 'ễ', 'ế', 'ệ', 'f', 'g', 'h', 'i', 'ì', 'ỉ', 'ĩ', 'í', 'ị', 'j', 'k', 
        'l', 'm', 'n', 'o', 'ò', 'ỏ', 'õ', 'ó', 'ọ', 'ô', 'ồ', 'ổ', 'ỗ', 'ố', 'ộ', 'ơ', 'ờ', 'ở', 'ỡ', 'ớ', 'ợ', 'p', 'q', 
        'r', 's', 't', 'u', 'ù', 'ủ', 'ũ', 'ú', 'ụ', 'ư', 'ừ', 'ử', 'ữ', 'ứ', 'ự', 'v', 'w', 'x', 'y', 'ỳ', 'ỷ', 'ỹ', 'ý', 'ỵ', 'z']

func = ['space', 'word']

while True:
    inp = input("Nhap: ")

    if (inp == 'q'):
        speak("Chào tạm biệt!")
        break
    elif (inp == 'd'):
        word = ""
        speak("Xoá toàn bộ")
    elif (inp == 'space'):
        word = word + " "
        speak("Dấu cách")
    elif (inp == 'word'):
        tam = word
        for i in range(0,len(tam)):
            if (tam[i] == "<"):
                char_index = alphabet.index(tam[i+1])
                temp = tam[i] + tam[i+1]
                temp_replaced = alphabet[char_index+4]
                word = tam.replace(temp, temp_replaced)
            elif (tam[i] == ">"):
                char_index = alphabet.index(tam[i+1])
                temp = tam[i] + tam[i+1]
                temp_replaced = alphabet[char_index+1]
                word = tam.replace(temp, temp_replaced)
            elif (tam[i] == "?"):
                char_index = alphabet.index(tam[i+1])
                temp = tam[i] + tam[i+1]
                temp_replaced = alphabet[char_index+4]
                word = tam.replace(temp, temp_replaced)
            elif (tam[i] == "~"):
                char_index = alphabet.index(tam[i+1])
                temp = tam[i] + tam[i+1]
                temp_replaced = alphabet[char_index+4]
                word = tam.replace(temp, temp_replaced)
            elif (tam[i] == "."):
                char_index = alphabet.index(tam[i+1])
                temp = tam[i] + tam[i+1]
                temp_replaced = alphabet[char_index+4]
                word = tam.replace(temp, temp_replaced)
        print(word)
        speak(word)
    else:
        if (inp in braille_encode):
            index = braille_encode.index(inp)
            word = word + alphabet[index]
            if (alphabet[index] == 'i'):
                text = "Chữ " + alphabet[index] + " ngắn"
            elif (alphabet[index] == 'y'):
                text = "Chữ " + alphabet[index] + " dài"
            else:
                text = "Chữ " + alphabet[index]
        #####################################################       
        elif (inp in tone_marks_encode):
            index = tone_marks_encode.index(inp)
            word = word + tone_marks[index]
            if (tone_marks[index] == "<"):
                text = "Dấu sắc"
            elif (tone_marks[index] == ">"):
                text = "Dấu huyền"
            elif (tone_marks[index] == "?"):
                text = "Dấu hỏi"
            elif (tone_marks[index] == "~"):
                text = "Dấu ngã"
            elif (tone_marks[index] == "."):
                text = "Dấu nặng"
        #####################################################
        else:
            text = "Ký tự không tồn tại"
        speak(text)

