% rebase('layout.tpl', title="Mnemonistka")

<!-- Begin page content -->
<main role="main" class="flex-shrink-0">
  <div class="container">


<div style="text-align:center; padding-top: 30px">
    <h1 class="mt-5">Опорные образы</h1>
    <p class="lead">Вы можете создавать свои последовательности опорных образов.<br>Опорные образы предназначены для запоминания информации на них.<br>Подробнее читайте в <a href='#'>теории</a>.<br>Вы можете редактировать цепочки, а также тренировать их запоминание.</p>

</div>
<br>


		<div style="text-align:center">
			<ul  style = "list-style-type:none">
		% for name in path_names:
			<li style="font-size: 24px;">{{name.name}}</li>
			<a href="/memory_training_path/{{name.name}}">Тренировка</a> ||
			<a href="/path/{{name.id}}">Смотреть таблицу</a> ||
			<a href="/path_name_edit/{{name.id}}">Изменить название таблицы</a> ||
			<a href="/path_delete/{{name.id}}">Удалить таблицу</a>
		% end
			</ul>
		</div>
		<br>
		<br>
		<div>
		<p>Добавить цепочку опорных образов:</p>

		<form action="/path" method="POST">
			<input type="text" size="50" maxlength="100" name="path_name">
		    <input type="submit" name="save" value="Сохранить название">
		</form>

		</div>


    
  </div>
</main>