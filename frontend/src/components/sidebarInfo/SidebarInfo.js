import Widget from "../widget/Widget"
import './SidebarInfo.scss';

const SidebarInfo = () => {

    return (
        <aside id="sidebar" className="grid-30">
            <Widget title='About me'>
                <div className="about_me">
                    <div className='avatar'>
                        <a href="#" className="thumb">
                            <img className="fullimage cover" alt="avatar" src="https://themes.estudiopatagon.com/wordpress/groovy/wp-content/uploads/2023/01/avatar-1.jpg"/>
                        </a>
                    </div>
                    <div className="info">
                        <h4 className="title small author-name">
                            <a href="#">Jonathan Doe</a>
                        </h4>
                        <p className="founder">Founder & Editor</p>
                    </div>
                </div>

                <p className="description">
                    Hello! My name is Jonathan Doe working from Chile. I create some Ghost and Wordpress themes for differents markets, also, i offer live support via our ticket system.
                </p>
            </Widget>
        </aside>
    )
}

export default SidebarInfo;
