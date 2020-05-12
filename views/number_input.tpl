% rebase('layout.tpl', title='Mnemotechnics')

<!-- Begin page content -->
<main role="main" class="flex-shrink-0">
  <div style='text-align:center; margin-top: 100px;' class="container">

 
<h1 class="mt-5">Ваш ответ:</h1>

<br>



<form action="/number_results" method="POST">
<div>
% count = 0
% for i in range(fields_amount):
% count += 1
<div>
	<label for="number{{count}}">{{count}}</label>
	<input id="number{{count}}" type="text" name="number{{count}}" value="">
</div>
% end

<input type="submit" value="Готово"/>
</div>
</form>


    
  </div>
</main>

