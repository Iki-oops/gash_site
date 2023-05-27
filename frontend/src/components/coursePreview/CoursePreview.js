import { FaArrowRight } from "react-icons/fa";

import './Course.scss';
import TagIcon from '../something/TagIcon';
import { monthNames } from '../../utils/monthNames';
import hexToRgb from '../../utils/hexToRgb';

const LessonPreview = (props) => {
    const {tags, created_at} = props;
    const firstTag = tags.length > 0 ? tags[0] : null;
    const backgroundColor = firstTag ? hexToRgb(tags[0].hex_color, 0.15) : null;
    const date = new Date(created_at);
    const formated_date = `${date.getDay()} ${monthNames[date.getMonth()]} ${date.getFullYear()}`;

    return (
        <View {...props} tag={firstTag} backgroundColor={backgroundColor} created_at={formated_date}/>
    )
}

const View = ({name, description, created_at, tag, backgroundColor}) => {
    return (
        <div className="bg-wrapper-box">
            <div className="lesson bg-box" style={{backgroundColor}}>
                <div className="lesson-thumb-wrapper">
                    <div className="lesson-thumb epcl-flex">
                        <a href="#" className="thumb">
                            <img className='fullimage' src="https://themes.estudiopatagon.com/wordpress/groovy/wp-content/uploads/2019/08/light-bulb-creative-business-idea-symbol-held-by-hand_53876-127176-1-450x500.jpg" alt="lesson-thumb"/>
                        </a>
                    </div>
                </div>
                <div className="info">
                    <header>
                        <div className='meta-wrapper epcl-flex'>
                            <div className='tags'>
                                {
                                    tag ?
                                    <a href="#" className='tag-link'>
                                        <TagIcon color={tag.hex_color} />
                                        <span>{tag.name}</span>
                                    </a> :
                                    null
                                }
                            </div>
                            <div className='meta'>
                                <time>{created_at}</time>
                            </div>
                        </div>
                        <div className='main-title title-large title'>
                            <a href="#" title={name}>
                                {name.length > 30 ? `${name.slice(0, 30)}...` : name}
                            </a>
                        </div>
                    </header>
                    <div className='lesson-descr'>
                        <p>
                            {description.length > 200 ? `${description.slice(0, 200)}...` : description}
                        </p>
                    </div>
                    <footer>
                        <div className='meta'>
                            <a href='#' className='epcl_button'>
                                <span>Continue Reading</span>
                                <FaArrowRight size='18px' style={{position: 'absolute', top: '10px', right: '25px'}}/>
                            </a>
                            <a href="#" title='Author: Jonathan Doe' className='meta-info author'>
                                <span className='author-image cover' style={{backgroundImage: 'url("https://themes.estudiopatagon.com/wordpress/groovy/wp-content/uploads/2023/01/avatar-1.jpg")'}}></span>
                                <span className='author-name'>Jonathan Doe</span>
                            </a>
                        </div>
                    </footer>
                </div>
            </div>
        </div>
    )
}

export default LessonPreview;
