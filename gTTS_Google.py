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

   
braille_decode = {
    '1': 'a', '12': 'b', '14': 'c', '145': 'd', '15': 'e', '124': 'f',
    '1245': 'g', '125': 'h', '24': 'i', '245': 'j', '13': 'k', '123': 'l', '134': 'm',
    '1345': 'n', '135': 'o', '1234': 'p', '12345': 'q', '1235': 'r', '234': 's', '2345': 't',
    '136': 'u', '1236': 'v', '2456': 'w', '1346': 'x', '13456': 'y', '1356': 'z',
    '345': 'ă', '16': 'â', '2346': 'đ', '126': 'ê', '1456': 'ô', '246': 'ơ', '1256': 'ư',
    '35': 'sắc', '56': 'huyền', '26': 'hỏi', '36': 'ngã', '6': 'nặng'
}
                
alphabet = ['a', 'à', 'ả', 'ã', 'á', 'ạ', 'ă', 'ằ', 'ẳ', 'ẵ', 'ắ', 'ặ', 'â', 'ầ', 'ẩ', 'ẫ', 'ấ', 'ậ', 'b', 'c', 'd', 'đ', 
        'e', 'è', 'ẻ', 'ẽ', 'é', 'ẹ', 'ê', 'ề', 'ể', 'ễ', 'ế', 'ệ', 'f', 'g', 'h', 'i', 'ì', 'ỉ', 'ĩ', 'í', 'ị', 'j', 'k', 
        'l', 'm', 'n', 'o', 'ò', 'ỏ', 'õ', 'ó', 'ọ', 'ô', 'ồ', 'ổ', 'ỗ', 'ố', 'ộ', 'ơ', 'ờ', 'ở', 'ỡ', 'ớ', 'ợ', 'p', 'q', 
        'r', 's', 't', 'u', 'ù', 'ủ', 'ũ', 'ú', 'ụ', 'ư', 'ừ', 'ử', 'ữ', 'ứ', 'ự', 'v', 'w', 'x', 'y', 'ỳ', 'ỷ', 'ỹ', 'ý', 'ỵ', 'z']


word = ""
text = ""
func = ['space', 'word']

while True:
    inp = input("Nhap: ").lower()
    
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
        n = len(tam)
        for i in range(0, n):
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
        
    else:  # for letters
        if (inp in braille_decode.keys()):
            letter = braille_decode[inp]
            word = word + letter
            
            if (letter == 'i'):
                text = "Chữ i ngắn"
            elif (letter == 'y'):
                text = "Chữ y dài"
            else:
                if letter in ["<", ">", "?", "~", "."]:
                    text = "Dấu " + letter
                else:
                    text = "Chữ " + letter
                    
        else:
            text = "Ký tự không tồn tại"
        speak(text)

