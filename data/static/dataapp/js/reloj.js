const $tiempo = document.querySelector('.tiempo'),
    $fecha = document.querySelector('.fecha');

function digitalClock() {
    let f = new Date(),
        dia = f.getDate(),
        mes = f.getMonth() + 1,
        anio = f.getFullYear(),
        diaSemana = f.getDay();

    dia = ('0' + dia).slice(-2);
    mes = ('0' + mes).slice(-2);

    let timeString = f.toLocaleTimeString();
    $tiempo.innerHTML = timeString;

    let semana = ['DOM', 'LUN', 'MAR', 'MIE', 'JUE', 'VIE', 'SAB'];
    let showSemana = (semana[diaSemana]);
    $fecha.innerHTML = `${anio}-${mes}-${dia} ${showSemana}`
}
setInterval(() => {
    digitalClock()
}, 1000);

$(document).ready(function () {
    $.get("https://api.gael.cloud/general/public/clima",
        function (data) {
            $.each(data, function (i, item) {
                if (i === 9) {
                    $("#clima").append(
                        "<tr><td>Ultima Actualizacion:  " + item.HoraUpdate +
                        "</td><td>Ciudad:  " + item.Estacion +
                        "</td><td>Temperatura:  " + item.Temp +"°c"+
                        "</td><td>Estado del Clima:  " + item.Estado + "</td></tr>");
                };
            });
        });
});