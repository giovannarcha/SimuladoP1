def buscar_livros(request):
    nome = request.GET.get('nome', '')
    tipo = request.GET.get('tipo', '')
    categoria = request.GET.get('categoria', '')

    livros = Livro.objects.all()

    if nome:
        livros = livros.filter(titulo__icontains=nome)
    if tipo:
        livros = livros.filter(tipo_acervo=tipo)
    if categoria:
        livros = livros.filter(categoria=categoria)

    return render(request, 'acervo/busca.html', {
        'livros': livros,
        'tipos': Livro.TIPO_ACERVO,
        'categorias': Livro.CATEGORIA_CDD,
    })