% rebase('layout.tpl', title='Mnemotechnics')


<!-- Begin page content -->
<main role="main" class="flex-shrink-0">
  <div style='text-align:center; margin-top: 100px;' class="container">

<h1>Результаты</h1>
<h1>{{results_status}}</h1>



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


<p>Общая статистика:</p>

<p>Всего побед: {{win_results}}</p>
<p>Всего поражений: {{loose_results}}</p>


<a style='margin-bottom: 20px;font-sixe:36px;' href="/number_memory">Ещё раз?</a>



    
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