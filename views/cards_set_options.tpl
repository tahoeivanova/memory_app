% rebase('layout.tpl', title='Mnemotechnics')

<!-- Begin page content -->
<main role="main" class="flex-shrink-0">
  <div class="container">
<div style="text-align:center; padding-top: 30px">
    <h1 class="mt-5">Тренировка игральных карт</h1>
    <p class="lead">Вам будут продемонстрированы игральные карты. Вы должны запомнить их последовательность и ввести ответ. Задайте параметры.</p>
</div>




<div style="text-align:center; padding-top: 50px">
<form action='/cards_memory' method="POST">
   <label for="cards_all">Количество карт</label>
  <select name="cards_all" id="inlineFormCustomSelectPref">
    <option selected value="36">36</option>
    <option value="52">52</option>
    <option value="54">54</option>
  </select>
<br>
<br>
    <label for="cards_time">Время на одну карту (секунды)</label>
    <input id="cards_time" type="text" name="cards_time" value="7">

<br>
<br>
    <input type="submit" value="Начали!"/>
</form>
</div>

  </div>
</main>