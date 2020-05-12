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
% percent = round((right_answer/count*100), 2)
<p>Процент правильных ответов: {{percent}} %</p>


<p>Общая статистика:</p>

<p>Всего побед: {{win_results}}</p>
<p>Всего поражений: {{loose_results}}</p>


<a style='margin-bottom: 20px;font-sixe:36px;' href="{{url}}">Ещё раз?</a>



    
  </div>
</main>
