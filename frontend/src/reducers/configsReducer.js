import { createReducer } from "@reduxjs/toolkit"

const initialState = {
    logoImg: 'https://frenify.com/work/envato/frenify/wp/oxxo/1/wp-content/themes/oxxo/framework/img/logo/mobile-retina-logo.png',
}

const configs = createReducer(initialState, () => {});

export default configs;
