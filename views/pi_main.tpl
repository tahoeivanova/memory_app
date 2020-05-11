% rebase('layout.tpl', title="Mnemotechnics")

<!-- Begin page content -->
<main role="main" class="flex-shrink-0">
  <div class="container">
<div style="text-align:center; padding-top: 30px">
    <h1 class="mt-5">Число Пи</h1>
    <p class="lead">Проверьте, сколько цифр числа Пи Вы знаете.<br>Задайте параметры.</p>
    <p class="lead">Чтобы посмотреть число Пи до определенного знака (до 1000 знаков), введите в браузерную строку после pi/ число знаков после запятой, например, pi/10.</p>

</div>




<div style="text-align:center; padding-top: 50px">
<form action='/pi' method="POST">
    <label for="pi_length">Количество цифр после запятой</label>
    <input id="pi_length" type="text" name="pi_length" value="10">
    <label for="pi_field_length">Количество цифр в одном поле для ввода</label>
    <input id="pi_field_length" type="text" name="pi_field_length" value="10">


<br>
<br>



    <input type="submit" value="Начали!"/>
</form>
</div>









    
  </div>
</main>

