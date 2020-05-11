% rebase('layout.tpl', title="Mnemotechnics")

<!-- Begin page content -->
<main role="main" class="flex-shrink-0">
  <div style='text-align:center; margin-top: 100px;' class="container">

 
<h1 class="mt-5">Ваш ответ:</h1>

<br>


<form action="/cards_results" method="POST">
<div>
% for number in range(1, len(card_list)+1):
    <br>

    <label for="card{{number}}">Карта {{number}} </label>

  <select name="card{{number}}" id="card{{number}}">
    <br>
    % for card in card_list:
    <option value="{{card}}">{{card}}</option>
    % end
  </select>
      <br>

% end
<br>

</div>
<input type="submit" value="Готово"/>

</form>



    
  </div>
</main>

