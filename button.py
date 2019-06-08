while True:
    print('What do you want the button to say:')
    linkText = input('Button Text: ').replace(r"'", r"\'")

    newLink = '<a class="chatSuggest" onclick="$(this).hide(); chatSuggest(\'' + linkText + '\')";>' + linkText + '</a>'
    print()
    print('==========================')
    print('Just copy and paste this into your knowledge base response:')
    print(newLink)
    print('==========================')
