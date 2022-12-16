def setUpInput(text):
    text = text.replace("sin", "np.sin")
    text = text.replace("cos", "np.cos")
    text = text.replace("tan", "np.tan")
    text = text.replace("cot", "1/np.tan")
    text = text.replace("sec", "1/np.cos")
    text = text.replace("csc", "1/np.sin")    
    text = text.replace("ln", "np.log")
    text = text.replace("^", "**")
    #text = text.replace("log", "np.log10")
    return text