def designerPdfViewer(h, word):
    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t', 'u','v','w','x','y' ,'z']
    index=[]
    for i in word:
        index.append(letters.index(i))

    area=[]
    for i in index:
        area.append(h[i])


    return len(word)*max(area)
         


h = list(map(int, input('len: ').rstrip().split()))
word = input('word: ')
print(designerPdfViewer(h, word))     