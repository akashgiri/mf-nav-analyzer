$(function() {
    var get_nav_change = (function ($) {
        var target_element = $("#nav-change-wrapper");
        var stocks_data_wrapper = $("#stocks-data-wrapper");
        var stocks_li = $("#stocks-data-wrapper li");
        var stock_count = $("#stocks-data-wrapper li").length;
        var result_span = $("#result");
        var loader_id = $("#loading");
        var url = "/funds/fund/nav_change/";
        var slug = target_element.attr("data-attr");

        var add_loader = function() {
            var loader_html = $("<img id='loading' src='/static/img/loading_icon.gif'>");
            target_element.after(loader_html);
        };

        var remove_loader = function() {
            $("#loading").remove();
        };

        var fetch_nav_change = function() {
            add_loader();
            $.ajax({
                url: url,
                type: 'GET',
                contentType: 'application/json',
                data: {
                    list: slug
                },
                dataType: 'json',
                success: function(response) {
                    remove_loader();
                    console.log(response);
                    var ch = response.ch;
                    result_span.css('visibility', 'visible');
                    result_span.html(ch);
                },
                error: function(response) {
                    console.log(response)
                }
            });
        };

        var init = function() {
            target_element.on("click", function() {
                fetch_nav_change();
            });
        };

        return {
            init: init
        }

    })(jQuery);
    get_nav_change.init();
});
