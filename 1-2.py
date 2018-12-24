def tokenizer(text):
    words = text.split(' ')
    tokenized_words = []
    for word in words:
        tokenized_words.append(word_tokenizer(word))
    return tokenized_words

#2-3에서 따옴표 앞,뒤,중간에 한글자만 있는지 확인하기 위한 메소드
#짝수번째 글자가 모두 ','면 'true'이고 홀수번째 글자가 모두 '.'가 아니면 'true'반환, 나머지 경우는 'false' 반환
def acronym(word):
    a = 'true'
    if len(word)%2 == 0:
        a = 'fasle'
    else :    
        for i in range(1, int((len(word)-1)/2)+1) :
            if word[2*i-1]!='.':
                a = 'false'
        for i in range(0, int((len(word)-1)/2)+1) :
            if word[2*i]=='.' :
                a = 'false'
    return a

def word_tokenizer(word):
    if ('.' not in word) and ('\'' not in word):
        return word
    else:
        if '\'' in word:
            # TODO - 따옴표로 시작해서 따옴표로 끝나는 단어의 따옴표 삭제, 단어 도중에 따옴표가 나오는 경우 따옴표 포함 뒤2의 글자 모두 삭제
            # 2-1 
          if word[0]=='\'' and word[len(word)-1]=='\'' :
              word = word[1:len(word)-1] 
              #단어 맨 처음과 끝이 따옴표면 따옴표 삭제
              if '\'' in word:
                  word = word[0:word.find('\'')] 
                  #맨 앞과 뒤의 따옴표 삭제후 남아있는 따옴표 뒤의 글자 삭제   
          else :
              word = word[0:word.find('\'')] 
              #따옴표 뒤의 글자 삭제 
               
        if '.' in word:
            # TODO - ".com"으로 끝나는 단어는 토큰화되지 않도록
            # TODO - 마침표로 연결된 단어에서 마침표 앞, 뒤 및 사이에 있는 글자가 모두 1개일 경우 마침표 삭제, 0개 혹은 2개 이상이면 토큰화되지 않도록
            #2-2
            if word[len(word)-4:len(word)]=='.com':
                pass
                # 맨뒤에 .com이 오면 pass
            #2-3    
            elif acronym(word) == 'true' :
                word = word.replace('.','')
            else :
                pass

        return word


if __name__ == '__main__':
    text = '''i've 'hello' 'hello'world' imlab's PH.D I.B.M snu.ac.kr 127.0.0.1 galago.gif ieee.803.99 naver.com gigabyte.tw pass..fail'''
    print(tokenizer(text))
    