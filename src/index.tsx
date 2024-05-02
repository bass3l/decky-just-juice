import {
  definePlugin,
  PanelSection,
  PanelSectionRow,
  ServerAPI,
  SliderField,
  staticClasses,
} from "decky-frontend-lib";
import { VFC } from "react";
import { FaBatteryHalf } from "react-icons/fa";
import useLocalStorage from "use-local-storage";

const CACHE_KEY = 'decky-just-juice';
const OFF = 0;
const ICON = 1;
const PERCENTAGE = 2;

const Content: VFC<{ serverAPI: ServerAPI }> = ({serverAPI}) => {

  const [currentConfig, setCurrentConfig] = useLocalStorage<number>(CACHE_KEY, 0);

  const onChange = async (level: number) => {
    switch (level) {
      case OFF:
        await serverAPI.callPluginMethod('disable_juice', {});
        break;
      case ICON:
        await serverAPI.callPluginMethod('enable_icon_juice', {});
        break;
      case PERCENTAGE:
        await serverAPI.callPluginMethod('enable_percentage_juice', {});
        break;
    }

    setCurrentConfig(level);
  };

  return (
    <PanelSection>
      <PanelSectionRow>
        <SliderField
          min={0}
          max={2}
          step={1}
          label="Overlay Level"
          bottomSeparator="none"
          notchTicksVisible={true}
          value={currentConfig}
          notchCount={3}
          notchLabels={[{
            notchIndex: OFF,
            label: 'Off',
            value: OFF,
          }, {
            notchIndex: ICON,
            label: 'Icon',
            value: ICON
          }, {
            notchIndex: PERCENTAGE,
            label: '%',
            value: PERCENTAGE
          }]}
          onChange={onChange}
        />
        <p style={{ fontSize: 14 }}>Might take a second to update.</p>
      </PanelSectionRow>
    </PanelSection>
  );
};

export default definePlugin((serverApi: ServerAPI) => {  
  return {
    title: <div className={staticClasses.Title}>Just Juice</div>,
    content: <Content serverAPI={serverApi} />,
    icon: <FaBatteryHalf />,
    onDismount() {},
  };
});
