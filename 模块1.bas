Attribute VB_Name = "模块1"
Sub 字体修改()
'
' 字体修改 宏
'
    Dim R_Character As Range


    Dim FontSize(5)
    ' 字体大小在5个值之间进行波动，可以改写
    FontSize(1) = "17"
    FontSize(2) = "17.5"
    FontSize(3) = "18"
    FontSize(4) = "18.5"
    FontSize(5) = "16.5"



    Dim FontName(3)
    '字体名称在三种字体之间进行波动，可改写，但需要保证系统拥有下列字体
    FontName(1) = "陈静的字完整版"
    FontName(2) = "贱萌体"
    FontName(3) = "李国夫手写体"

    Dim ParagraphSpace(3)
    '行间距 在一定以下值中均等分布，可改写
    ParagraphSpace(1) = "1"
    ParagraphSpace(2) = "2"
    ParagraphSpace(3) = "0"

    '不懂原理的话，不建议修改下列代码

    For Each R_Character In ActiveDocument.Characters

        VBA.Randomize

        R_Character.Font.Name = FontName(Int(VBA.Rnd * 3) + 1)

        R_Character.Font.Size = FontSize(Int(VBA.Rnd * 5) + 1)

        R_Character.Font.Position = Int(VBA.Rnd * 3) + 1

        R_Character.Font.Spacing = 0


    Next

    Application.ScreenUpdating = True



    For Each Cur_Paragraph In ActiveDocument.Paragraphs

        Cur_Paragraph.LineSpacing = ParagraphSpace(Int(VBA.Rnd * 3) + 1)


    Next
        Application.ScreenUpdating = True


End Sub
