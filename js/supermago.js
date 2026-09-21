;(() => {
    /************
     * Versão do Script
     ************/
    const SCRIPT_VERSION = "1.0.3";

    /************
     * Console *
     ************/
    const mensagemConsole = `%cSuper Mago (v${SCRIPT_VERSION})\n%cOtimizando o rastreamento das vendas desse site\n%cAcesse https://meusupermago.com e saiba como gastar menos e lucrar muito mais com suas campanhas de tráfego pago.`;
    const estilos = [
        'font-size: 20px; font-weight: bold; color: #022260;',
        'font-size: 16px; color: #022260;',
        'font-size: 14px; color: #022260;',
    ];
    console.log(mensagemConsole, ...estilos);
    console.log(`SUPERMAGO UTMs Script - iniciado (versão ${SCRIPT_VERSION})`);

    /****************
     * UTM Handler  *
     ****************/
    class UTMHandler {
        static ORDER = ['utm_campaign', 'utm_medium', 'utm_source', 'utm_content', 'utm_term'];

        static fixMalformedUrl(url) {
            const parts = url.split("?");
            if (parts.length > 2) {
                const base = parts.shift();
                const query = parts.join("&");
                return `${base}?${query}`;
            }
            return url;
        }

        static getUtmParamsFromLocation() {
            return new URLSearchParams(window.location.search);
        }

        static buildUtmPipeString() {
            const r = UTMHandler.getUtmParamsFromLocation();
            return UTMHandler.ORDER
                .map(key => (r.get(key) ?? ''))
                .join('|');
        }

        static hasAnyUtmValue(pipeString) {
            return pipeString.split('|').some(v => v.trim() !== '');
        }

        static isHotmartLink(url) {
            return /(^|\.)hotmart\.com/i.test(new URL(url, window.location.origin).hostname);
        }

        // Para links NÃO Hotmart: replica utm_* atuais.
        static addUtmParametersToUrl(url) {
            url = UTMHandler.fixMalformedUrl(url);
            const newUrl = new URL(url, window.location.origin);
            const pageParams = UTMHandler.getUtmParamsFromLocation();

            UTMHandler.ORDER.forEach(key => {
                const value = pageParams.get(key);
                if (value !== null && value !== undefined) {
                    newUrl.searchParams.set(key, value);
                }
            });

            return newUrl.toString();
        }

        // Para links Hotmart: zera utm/src/sck e seta sck (antes) e src (depois) com a MESMA string.
        static addUtmToHotmartUrl(url) {
            url = UTMHandler.fixMalformedUrl(url);
            const newUrl = new URL(url, window.location.origin);

            [...UTMHandler.ORDER, 'src', 'sck'].forEach(param => newUrl.searchParams.delete(param));

            const pipe = UTMHandler.buildUtmPipeString();

            if (UTMHandler.hasAnyUtmValue(pipe)) {
                newUrl.searchParams.append('sck', pipe); // primeiro
                newUrl.searchParams.append('src', pipe); // depois
            }

            return newUrl.toString();
        }
    }

    /**********************
     * Reescrita de Links *
     **********************/
    function updateLinks() {
        let linksReescritos = 0;
        document.querySelectorAll("a[href]").forEach(link => {
            const href = link.getAttribute('href');
            if (!href || href === "#" || href.trim().toLowerCase().startsWith("javascript:")) return;

            try {
                const absolute = new URL(href, window.location.origin).href;
                const newUrl = UTMHandler.isHotmartLink(absolute)
                    ? UTMHandler.addUtmToHotmartUrl(absolute)
                    : UTMHandler.addUtmParametersToUrl(absolute);

                if (newUrl && newUrl !== link.href) {
                    link.href = newUrl;
                    linksReescritos++;
                }
            } catch (err) {
                console.error("Erro ao processar link:", href, err);
            }
        });
        console.log(`${linksReescritos} link(s) reescrito(s)`);
    }

    /**********************
     * Reescrita de Forms *
     **********************/
    function updateForms() {
        document.querySelectorAll("form[action]").forEach(form => {
            const action = form.getAttribute('action');
            if (!action) return;

            try {
                const absolute = new URL(action, window.location.origin).href;
                const newAction = UTMHandler.isHotmartLink(absolute)
                    ? UTMHandler.addUtmToHotmartUrl(absolute)
                    : UTMHandler.addUtmParametersToUrl(absolute);

                if (newAction) form.action = newAction;
            } catch (err) {
                console.error("Erro ao processar formulário:", action, err);
            }
        });
    }

    /*************************
     * Intercepta window.open *
     *************************/
    function interceptWindowOpen() {
        const originalOpen = window.open;
        window.open = function (url, name, specs) {
            try {
                const absolute = new URL(url, window.location.origin).href;
                const newUrl = UTMHandler.isHotmartLink(absolute)
                    ? UTMHandler.addUtmToHotmartUrl(absolute)
                    : UTMHandler.addUtmParametersToUrl(absolute);
                return originalOpen.call(window, newUrl, name || "", specs || "");
            } catch (err) {
                console.error("Erro ao processar window.open:", url, err);
                return originalOpen.call(window, url, name || "", specs || "");
            }
        };
    }

    /***************
     * Inicializa  *
     ***************/
    function initialize() {
        updateLinks();
        updateForms();
        interceptWindowOpen();

        const repeatUpdates = () => {
            updateLinks();
            updateForms();
            [2000, 3000, 5000, 9000].forEach(delay => {
                setTimeout(() => {
                    updateLinks();
                    updateForms();
                }, delay);
            });
        };

        if (document.readyState === "complete") {
            repeatUpdates();
        } else {
            window.addEventListener("load", repeatUpdates);
        }
    }

    initialize();
})();

