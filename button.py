import pyperclip

print('##################################################')
print('If you are running this on PythonAnywhere, you should run this command instead:')
print('python3 buttonPE.py')
print('##################################################')
print('')

while True:
    print('What do you want the button to say:')
    linkText = input('Button Text: ')

    print('What do you want to send to the ChatBot (leave blank to send button text):')
    queryText = input('Query Text: ').replace(r"'", r"\'")

    if queryText == "":
        queryText = linkText.replace(r"'", r"\'")

    newLink = '<a class="chatSuggest" onclick="$(this).hide(); chatSuggest(\'' + queryText + '\')";>' + linkText + '</a><br>'
    pyperclip.copy(newLink)
    print()
    print()
    print('====================================================')
    print('Just copy and paste this into your knowledge base response:')
    print(newLink)
    print('====================================================')
    print()
    print()
