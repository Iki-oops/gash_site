import { useHttp } from "../hooks/http.hook";

const useMarvelService = () => {
	const { request } = useHttp();

	const _apiBase = "api/v1/";
	// ЗДЕСЬ БУДЕТ ВАШ КЛЮЧ, ЭТОТ КЛЮЧ МОЖЕТ НЕ РАБОТАТЬ
	// const _apiKey = "apikey=c5d6fc8b83116d92ed468ce36bac6c62";
	const _baseOffset = 210;

	const getAllLessons = async (offset = _baseOffset) => {
		const res = await request(
			`${_apiBase}lessons`
		);
		return res.data.results.map(_transformCharacter);
	};

	const _transformCharacter = (char) => {
		return {
			id: char.id,
			name: char.name,
			description: char.description
				? `${char.description.slice(0, 210)}...`
				: "There is no description for this character",
			thumbnail: char.thumbnail.path + "." + char.thumbnail.extension,
			homepage: char.urls[0].url,
			wiki: char.urls[1].url,
			comics: char.comics.items,
		};
	};


	return {
        getAllLessons,
	};
};

export default useMarvelService;
