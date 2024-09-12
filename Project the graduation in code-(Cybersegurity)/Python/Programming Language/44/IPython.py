from IPython.display import HTML

html_code = ""

<!DOCTYPE html>

<html lang="pt-br">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Meu Perfil</title>

</head>

<body style="font-family: 'Arial', sans-serif; background-color: #f8f8f8; margin: 0; padding: 0;">

 

    <header style="text-align: center; background-color: #FFC0CB; color: #fff; padding: 20px;">

        <h1 style="margin: 0;">Tassiana Milka</h1>

        <p style="margin: 5px 0;">Estudante de tecnologia</p>

    </header>

 

    <section style="margin: 20px; text-align: center;">

       <!--- <img src="content/sua_foto.jpg" alt="Sua Foto" style="border-radius: 50%; margin-bottom: 20px;">--->

        <div id="informacoes-pessoais" style="max-width: 400px; margin: 0 auto;">

            <p>Cidade: Campinas </p>

            <p>País: Brasil</p>

            <p>Interesses: Desing,Back-end e  Front-end.</p>

        </div>

    </section>

 

    <section style="margin: 20px; text-align: center;">

        <h2>Habilidades</h2>

        <ul style="list-style: none; padding: 0;">

            <li>Linguagens:Java,C,C++,C#,Ruby e etc.</li>

            <li>Ferramentas: Git, VS Code</li>

        </ul>

    </section>

 

    <section style="margin: 20px; text-align: center;">

        <h2>Projeto Recente</h2>

        <p>Trabalhando em um site pessoal para mostrar meu portfólio.</p>

    </section>

 

    <footer style="text-align: center; margin-top: 20px;">

        <a href="https://github.com/TassianaMilka" target="_blank" style="margin: 0 10px; color: #3498db; text-decoration: none;">Github </a>

    </footer>

</body>

</html>

 

# Exibindo a página HTML

HTML(html_code)
