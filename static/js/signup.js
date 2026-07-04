document.addEventListener(
    "DOMContentLoaded",
    initializeSignup
);

function initializeSignup() {

    document
        .getElementById("signupBtn")
        .addEventListener("click", signup);

    document
        .getElementById("googleBtn")
        .addEventListener("click", signInWithGoogle);

    document
        .getElementById("githubBtn")
        .addEventListener("click", signInWithGithub);

}

async function signup() {

    const email =
        document.getElementById("email").value;

    const password =
        document.getElementById("password").value;

    const { data, error } =
        await signupWithEmail(
            email,
            password
        );

    if (error) {

        alert(error.message);
        return;

    }

    if (data.session) {

        const result =
            await createBackendSession(
                data.session.access_token
            );

        if (result.success) {

            window.location.href = "/dashboard/";
            return;

        }

    }

    alert(
        "Please verify your email before logging in."
    );

    window.location.href = "/login/";

}