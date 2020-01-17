from django.shortcuts import render
from django.http import FileResponse
from django.views.generic import View
from reportlab.pdfgen import canvas
import io

from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML

# Create your views here.
class IndexView(View):

    def get(self, request, *args, **kwargs):
        # Cria um arquivo para receber os dados e gerar o PDF
        buffer = io.BytesIO()

        # Cria o arquivo PDF
        pdf = canvas.Canvas(buffer)

        # Insere 'coisas' no PDF
        pdf.drawString(100, 100, 'Xandão')

        # Quando acabamos de inserir coisas no PDF
        pdf.showPage()
        pdf.save()

        # Por fim, retornamos o buffer para o início do arquivo
        buffer.seek(0)

        # Faz o download do arquivo em PDF gerado
        # return FileResponse(buffer, as_attachment=True, filename='relatorio1.pdf')

        # Abre o PDF direto no navegador
        return FileResponse(buffer, filename='relatorio1.pdf')

class Index2View(View):

    def get(self, request, *args, **kwargs):
        texto = ['Xandão', 'X-a-n-d-ã-o', 'Texto Xandão']

        # Renderiza o conteúdo ai
        html_string = render_to_string('relatorio.html', {'texto': texto})

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/relatorio2.pdf')

        fs = FileSystemStorage('/tmp')

        with fs.open('relatorio2.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            # Faz o download do arquivo PDF
            # response['Content-Disposition'] = 'attachment; filename="relatorio2.pdf"'

            # Abre o PDF direto no navegador
            response['Content-Disposition'] = 'inline; filename="relatorio2.pdf"'
        return response
