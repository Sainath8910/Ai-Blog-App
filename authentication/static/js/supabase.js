/*
|--------------------------------------------------------------------------
| AI Blog Generator
| Supabase Client
|--------------------------------------------------------------------------
*/

(function () {

    if (!window.supabase) {

        console.error("Supabase SDK not loaded.");

        return;

    }

    if (!window.SUPABASE_URL || !window.SUPABASE_ANON_KEY) {

        console.error("Supabase configuration missing.");

        return;

    }

    window.supabaseClient = window.supabase.createClient(

        window.SUPABASE_URL,

        window.SUPABASE_ANON_KEY

    );

    console.log("✅ Supabase Client Initialized");

})();