% rebase('layout.tpl', title='Mnemotechnics')

<main role="main" class="flex-shrink-0">
  <div class="container">
<div style="text-align:center; padding-top: 30px">
    <h1 class="mt-5">Тренировка числовых образов</h1>
    <p class="lead">Вам будут продемонстрированы карточки с цифрами. Вы должны запомнить их и ввести ответ. Задайте параметры.</p>
</div>
<div style="text-align:center; padding-top: 50px">
<form action='/number_memory' method="POST">
    <label for="numbers_all">Количество карточек</label>
    <input id="numbers_all" type="text" name="numbers_all" value="10">
<br>
<br>
    <label for="digits_in_number">Количество цифр в карточке</label>
  <select name="digits_in_number" id="inlineFormCustomSelectPref">
    <option selected value="2">2</option>
    <option value="1">1</option>
  </select>
<br>
<br>
    <label for="number_time">Время на одну карточку (секунды)</label>
    <input id="number_time" type="text" name="number_time" value="7">

<br>
<br>
    <input type="submit" value="Начали!"/>
</form>
</div>
    
  </div>
</main>