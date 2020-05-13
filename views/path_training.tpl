% rebase('layout.tpl', title='Mnemotechnics')


<!-- Begin page content -->
<main role="main" class="flex-shrink-0">
  <div class="container">
  

<div id="carouselExampleInterval" class="carousel slide" data-ride="carousel">
  <div class="carousel-inner">

    <div class="carousel-item active" data-interval="1000">
      <div style="background-color: black; height: 300px;" class="d-block w-100"></div>
          <div class="carousel-caption d-none d-sm-block">
          <h1 style='margin-top: -150px; font-size: 72px;'>Старт!</h1>
        </div>
    </div>
% count = 0
% for number in random_numbers_global:
% count+=1

    <div class="carousel-item" data-interval="{{number_time}}" >
      <div style="background-color: black; height: 300px;" class="d-block w-100"></div>

        <div class="carousel-caption d-none d-sm-block">
          <h1 style='margin-top: -150px; font-size: 72px;'>{{number}}</h1>
          <p style='margin-top: -190px; color:grey;'>{{count}}/{{numbers_all}}</p>
        </div>

    </div>

        % end
    <div class="carousel-item" data-interval="10000" >

      <div style="background-color: black; height: 300px;" class="d-block w-100"></div>

        <div class="carousel-caption d-none d-sm-block">
          <h1 style='margin-top: -150px; font-size: 72px;'>Финиш!</h1>
        </div>

    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleInterval" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleInterval" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
</div>


<br>
<div style="text-align: center;">
<form action="/path_input" method="POST">
    <input type="submit" value="Готово!">
</form>  
</div>


  </div>
</main>

<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
      <script>window.jQuery || document.write('<script src="/docs/4.4/assets/js/vendor/jquery.slim.min.js"><\/script>')</script><script src="/docs/4.4/dist/js/bootstrap.bundle.min.js" integrity="sha384-6khuMg9gaYr5AxOqhkVIODVIvm9ynTT5J4V1cfthmT+emCG6yVmEZsRHdxlotUnm" crossorigin="anonymous"></script>

<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>