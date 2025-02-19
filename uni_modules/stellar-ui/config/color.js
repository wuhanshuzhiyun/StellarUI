import store from '../utils/store.js';
import Vuex from 'vuex';
let $state = new Vuex.Store({
	state: {
		steThemeColor: '#0090FF',
		defaultColor: '#0090FF',
	},
}).state;

function useColor() {
	return {
		setColor(params) {
			$state.steThemeColor = params.steThemeColor ?? $state.steThemeColor;
		},
		getColor() {
			return $state;
		},
		/**响应式数据*/
		$state,
	};
}
export default useColor;
