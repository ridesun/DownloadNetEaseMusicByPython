Attribute VB_Name = "ģ��1"
Sub �����޸�()
'
' �����޸� ��
'
    Dim R_Character As Range


    Dim FontSize(5)
    ' �����С��5��ֵ֮����в��������Ը�д
    FontSize(1) = "17"
    FontSize(2) = "17.5"
    FontSize(3) = "18"
    FontSize(4) = "18.5"
    FontSize(5) = "16.5"



    Dim FontName(3)
    '������������������֮����в������ɸ�д������Ҫ��֤ϵͳӵ����������
    FontName(1) = "�¾�����������"
    FontName(2) = "������"
    FontName(3) = "�������д��"

    Dim ParagraphSpace(3)
    '�м�� ��һ������ֵ�о��ȷֲ����ɸ�д
    ParagraphSpace(1) = "1"
    ParagraphSpace(2) = "2"
    ParagraphSpace(3) = "0"

    '����ԭ��Ļ����������޸����д���

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
