from django.http import HttpResponse

def handler404(request, exception):
     return HttpResponse("""
        <html>
            <body style="background-color: black;">
            <div style="text-align: center; margin-top: 50px; background-color: black; padding: 20px;">
                <h1 style="font-size: 48px; color: white;">404: Page not Found!</h1>
                <a href="/" style="display: inline-block; margin-top: 10px; padding: 10px 20px; background-color: white; color: black; text-decoration: none; font-weight: bold; border-radius: 5px;">Return Home</a>
            </div>
            </body>
        </html>
    """, status=404)