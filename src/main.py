from textnode import TextNode, TextType
print("hello world")
def main():
    test = TextNode("anchor text", TextType.LINK, "https://www.google.com")
    print(test)
main()
