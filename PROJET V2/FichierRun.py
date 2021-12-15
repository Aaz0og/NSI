    for elemy in y: 
                for elemx1 in x:
                    print("elemx1:",elemx1,"elemy:",elemy,"Stock:",stock)
                    if elemx1-stock  == elemy or elemx1 == elemy:
                        sol+= 1
                    print("Solution:",sol)
                    stock = elemx1
        