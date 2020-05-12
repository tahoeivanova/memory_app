%rebase('layout.tpl', title='Mnemotechnics')

<!-- Begin page content -->
<main role="main" class="flex-shrink-0">
  <div style='text-align:center; margin-top: 100px;' class="container">

 
<h1 class="mt-5">Введите {{pi_length}} цифр после запятой</h1>
<p class="lead">По {{pi_field_length}} цифр в каждом поле</p>




<br>
<h1 class="mt-5">3,...</h1>



<form action="/pi_results" method="POST">
<div>
% count = 0
% for i in range(0, pi_length, pi_field_length):
% count += 1
<div>
    <label for="pi_answer{{count}}"></label>
    <input id="pi_answer{{count}}" type="text" width="100" name="pi_answer{{count}}" value="">
</div>
%end
<br>

<input type="submit" value="Готово"/>
</div>
</form>

    
  </div>
</main>
