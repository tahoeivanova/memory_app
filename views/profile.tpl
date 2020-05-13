% rebase('layout.tpl', title='Mnemotechnics')
<!--     <link href="static/css/dashboard.css" rel="stylesheet">
 -->



    <main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-4">
      <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
        <h1 class="h2">Hello, {{user}}</h1>

      </div>

<!--       <canvas class="my-4 w-100" id="myChart" width="900" height="380"></canvas>
 -->
      <h2>Mnemonistka Profile</h2>
      <div class="table-responsive">
        <table class="table table-striped table-sm">
          <thead>
            <tr>
              <th>Numbers</th>
              <th>Cards</th>
              <th>Pi</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>{{results_number}}</td>
              <td>{{results_cards}}</td>
              <td>{{results_pi}}</td>
  
            </tr>
            
          </tbody>
        </table>
      </div>
    </main>

