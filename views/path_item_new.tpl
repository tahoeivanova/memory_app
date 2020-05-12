% rebase('layout.tpl', title="Mnemotechnics")

<div style="text-align:center">

<p>Add a new item to the Path: {{path}}</p>


<form action="/new_item/{{path}}" method="POST">
    <input type="text" size="100" maxlength="100" name="item">
    <input type="submit" name="save" value="save">

</form>



