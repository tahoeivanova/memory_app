<!doctype html>
<html lang="en" class="h-100">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Jekyll v3.8.6">
    <title>Sticky Footer Navbar Template · Bootstrap</title>

    <link rel="stylesheet" href="static/css/css_grid.css">

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">


    <link rel="canonical" href="https://getbootstrap.com/docs/4.4/examples/sticky-footer-navbar/">

    <!-- Bootstrap core CSS -->
<link href="/docs/4.4/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <!-- Favicons -->
<link rel="apple-touch-icon" href="/docs/4.4/assets/img/favicons/apple-touch-icon.png" sizes="180x180">
<link rel="icon" href="/docs/4.4/assets/img/favicons/favicon-32x32.png" sizes="32x32" type="image/png">
<link rel="icon" href="/docs/4.4/assets/img/favicons/favicon-16x16.png" sizes="16x16" type="image/png">
<link rel="manifest" href="/docs/4.4/assets/img/favicons/manifest.json">
<link rel="mask-icon" href="/docs/4.4/assets/img/favicons/safari-pinned-tab.svg" color="#563d7c">
<link rel="icon" href="/docs/4.4/assets/img/favicons/favicon.ico">
<meta name="msapplication-config" content="/docs/4.4/assets/img/favicons/browserconfig.xml">
<meta name="theme-color" content="#563d7c">


    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
.grid_input {
  display:grid;
  grid-template-columns: 250px 250px 250px 250px;
  grid-auto-flow: row;
  grid-auto-rows: minmax(20px, auto);
  grid-gap: 20px;
  margin: 100px;


}

.grid_input form {
  font-size: 12px;
  background-color: #778899;
  border: 1px solid #000000;
  border-radius: 5px;
  color: white;
  align-items: center;
  justify-content: center;
  padding: 10px;
}

.grid_input div{
  font-size: 12px;
  background-color: #778899;
  border: 1px solid #000000;
  border-radius: 5px;
  color: white;
}

.grid {
  display:grid;
  grid-template-columns: repeat(2, 2fr);
  grid-template-rows: 100px 100px 100px;
  grid-auto-rows: minmax(100px, auto);
  grid-column-gap: 20px;
  grid-row-gap: 20px;
  margin: 50px;


}

.grid div{
  font-size: 26px;
  background-color: green;
  border: 1px solid #000000;
  border-radius: 5px;
  color: white;
  justify-content: center;
  align-items: center;


}

.grid .another_color{
  background-color: #2F4F4F;
  
}

.grid .mistake_color{
  background-color: red;
  
}


    </style>
    <!-- Custom styles for this template -->
    <link href="sticky-footer-navbar.css" rel="stylesheet">
  </head>
  <body class="d-flex flex-column h-100">
    <header>
  <!-- Fixed navbar -->
  <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
    <a class="navbar-brand" href="/">Мнемотехника</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarCollapse">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/digits">Цифры</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/training_path">Опорные образы</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/pi">Число Пи</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/cards">Карты</a>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Теория</a>
        </li>
      </ul>
    </div>
  </nav>
</header>

<!-- Begin page content -->
<main role="main" class="flex-shrink-0">
  <div style='text-align:center; margin-top: 100px;' class="container">

<h1>Вы проиграли...</h1>
<h1>Ответы и ошибки</h1>



<div class="grid">

	<div>Ваш ответ</div>
	<div>Правильный ответ</div>

% right_answer = 0
% wrong_answer = 0
% count = 0
% for i,j in zipped_list:
% count+=1
  % if i==j:
  % right_answer+=1

	
  	<div>{{i}}</div>
  	<div>{{j}}</div>

  % else:
  % wrong_answer +=1
	<div class="mistake_color">{{i}}</div>
	<div class="mistake_color">{{j}}</div>
% end
% end
	
</div>

<p>Всего: {{count}}</p>
<p>Неправильных ответов: {{wrong_answer}}</p>
<p>Правильных ответов: {{right_answer}}</p>
% percent = right_answer/count*100
<p>Процент правильных ответов: {{percent}} %</p>

<p>Всего поражений: {{digit_results}}</p>


<a style='margin-bottom: 20px;font-sixe:36px;' href="/digits">Ещё раз?</a>



    
  </div>
</main>

<footer class="footer mt-auto py-3">
  <div class="container">
    <span class="text-muted">Mnemonistka by AraxnoAnarxo</span>
  </div>
</footer>
<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
      <script>window.jQuery || document.write('<script src="/docs/4.4/assets/js/vendor/jquery.slim.min.js"><\/script>')</script><script src="/docs/4.4/dist/js/bootstrap.bundle.min.js" integrity="sha384-6khuMg9gaYr5AxOqhkVIODVIvm9ynTT5J4V1cfthmT+emCG6yVmEZsRHdxlotUnm" crossorigin="anonymous"></script></body>
</html>